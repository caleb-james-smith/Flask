# display_fed_data.py

import tools
import datetime
import requests
from flask import Flask, render_template

# TODO
# - Only put FED status logic in python (not html): save as a new variable

# DONE
# - Get FED status based on multiple variables
# - Do not include non-FED rows in FED status counts
# - Do not include non-FED rows html table: remove rows
# - Right justify entries in table
# - Make columns wider in table
# - Change to a better font
# - Make background colors (gray, green, red, etc.) transparent
# - Add "Refresh" button at the top.
# - Add date and time at the top: fix issue with javascript.
# - Customize browser tab icon and name: fix issue with icon.
# - Move refresh code to javascript file.
# - Sort by any column (hardcoded)
# - Sort by FED number
# - Freeze header row so that it is always visible
# - Make Refresh button smaller; move to same row as date and time.
# - Sort by any column (specified by user) 
# - Do not include high-rate FEDs
# - Load live FED data in json format using requests library

app = Flask(__name__)

# Display FED data from input json file.

# for a dict in the table, print keys and values
def print_table_dict(input_data, my_key):
    my_dict = input_data["table"][my_key]
    for key, value in my_dict.items(): 
        print("{0}: {1}".format(key, value))

# for a list in the table, print keys and values
def print_table_list(input_data, my_key):
    my_list = input_data["table"][my_key]
    for element in my_list:
        this_key    = element["key"]
        this_type   = element["type"]
        print("{0}: {1}".format(this_key, this_type))

# for rows in the table, print a specific keys and values
def print_table_rows(input_data, my_keys):
    my_rows = input_data["table"]["rows"]
    for row in my_rows:
        message = ""
        for key in my_keys:
            value = row[key]
            # check if message is not empty
            if message:
                message += ", {0}: {1}".format(key, value)
            else:
                message += "{0}: {1}".format(key, value)
        print(message)

# process data
def process_data(input_data):
    # only include rows that are pixel FEDs that we want to keep
    output_data = [row for row in input_data if isPixFED(row) and keepPixFED(row)]
    return output_data

# sort data based on variable, reverse sorting also supported
def sort_data(input_data, variable, reverse=False):
    output_data = sorted(input_data, key=lambda x: x[variable], reverse=reverse)
    return output_data

# check if row is a pixel FED based on the board code.
def isPixFED(row):
    # note: the correct board code is "PIX FED ", including the space at the end
    answer = "PIX FED "
    board_code = row["BoardCode"]
    if board_code == answer:
        return True
    else:
        return False

# determine which FEDs to keep: do not keep high-rate FEDs
def keepPixFED(row):
    highrate_cutoff = 1400
    # check that connectionName is filled (not empty) before converting to int
    if row["connectionName"]:
        fed_number = int(row["connectionName"])
        # do not keep high-rate FEDs
        if fed_number >= highrate_cutoff:
            return False
        else:
            return True
    else:
        return False

# get FED status (0: error, 1: ok) based on variables
def getFEDStatus(row, variables):
    for variable in variables:
        value = row[variable]
        if value != 0:
            return 0
    return 1

# count number of FEDs in a certain status based on variables
def get_counts(table_rows, variables):
    counts = {}
    
    n_total     = 0
    n_running   = 0
    n_ready     = 0
    n_ok        = 0
    n_error     = 0
    
    for row in table_rows:
        n_total += 1
        # count FEDs in various states
        if row["stateName"] == "Running":
            n_running += 1
        if row["TTSState"] == "RDY":
            n_ready += 1
        # get FED status based on variables
        status = getFEDStatus(row, variables)
        if status:
            n_ok += 1
        else:
            n_error += 1

    counts["n_total"]   = n_total
    counts["n_running"] = n_running
    counts["n_ready"]   = n_ready
    counts["n_ok"]      = n_ok
    counts["n_error"]   = n_error
    
    return counts

# get data from collection point
def getData(url, proxies):
    try:
        page = requests.get(url, proxies=proxies)
        return page.json()
    except:
        print("ERROR:")
        print("    Failed to get data from '{0}'".format(url))
        print("    using these proxies: {0}.".format(proxies))
        print("Make sure that you are running an ssh tunnel with port forwarding using the correct ports to access this site.")
        return None

# use html template with conditional statements and loops
@app.route('/display_fed_data')
def result():
    raw_data = None
    use_local_json = False
    
    # FEDMonitor data from collection point in json format
    url = "http://kvm-s3562-3-ip157-27.cms:9945/urn:xdaq-application:lid=16/retrieveCollection?fmt=json&flash=urn:xdaq-flashlist:FEDMonitor"
    
    # proxies for CMS P5
    proxies = {
        "http" : "socks5h://127.0.0.1:1030",
        "https": "socks5h://127.0.0.1:1030"
    }    
    
    if use_local_json:
        # input json file with data
        #input_file  = "data/FEDMonitor_2023_09_01_v2.json"
        input_file  = "data/FEDMonitor_2023_09_26_v1_pretty.json"
        
        # load data from json file
        raw_data    = tools.load_data(input_file)
    else:
        raw_data = getData(url, proxies)
        #print("raw_data type: {0}".format(type(raw_data)))
        #print("raw_data: {0}".format(raw_data))
    
    # print data
    #print("--------------------")
    #tools.print_key_depth(raw_data)
    #print("--------------------")
    #print_table_dict(raw_data, "properties")
    #print("--------------------")
    #print_table_list(raw_data, "definition")
    #print("--------------------")
    #print_table_rows(raw_data, ["connectionName", "EvtErrNumTot", "RocErrNumTot"])
    #print("--------------------")
    
    if not raw_data:
        print("ERROR: Did not load data!")
        return render_template('data_error.html')
    
    # format data
    table_rows = process_data(raw_data["table"]["rows"])
    
    # sort data: default sorting when page first loads
    sorted_rows = sort_data(table_rows, "connectionName")
    #sorted_rows = sort_data(table_rows, "connectionName", True)
    #sorted_rows = sort_data(table_rows, "EvtErrNumTot")
    #sorted_rows = sort_data(table_rows, "RocErrNumTot")
    
    # get counts
    fed_counts = get_counts(table_rows, ["EvtErrNumTot", "RocErrNumTot"])
    
    return render_template('display_fed_data.html', fed_counts=fed_counts, fed_data=sorted_rows)

if __name__ == '__main__':
    app.run(port=4000, debug=True)

