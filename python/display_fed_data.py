# display_fed_data.py

import tools
import datetime
from flask import Flask, render_template

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

# format data as a sorted list of dictionaries
def format_data(input_data):
    output_data = []
    # sort keys: make sure to use list() so that sort() works!
    keys = list(input_data.keys())
    keys.sort()
    for key in keys:
        output_data.append(input_data[key])
    return output_data

# count status codes
def get_counts(input_data):
    counts = {}
    
    n_total = 0
    n_ok    = 0
    n_error = 0
    
    for row in input_data:
        n_total += 1
        if row["EvtErrNumTot"] == 0:
            n_ok += 1
        else:
            n_error += 1

    counts["n_total"]   = n_total
    counts["n_ok"]      = n_ok
    counts["n_error"]   = n_error
    
    return counts

# use html template with conditional statements and loops
@app.route('/display_fed_data')
def result():
    # input json file with data
    input_file  = "data/FEDMonitor_2023_09_01_v2.json"
    # load data from json file
    raw_data    = tools.load_data(input_file)
    # print data
    print("--------------------")
    tools.print_key_depth(raw_data)
    print("--------------------")
    print_table_dict(raw_data, "properties")
    print("--------------------")
    print_table_list(raw_data, "definition")
    print("--------------------")
    print_table_rows(raw_data, ["connectionName", "EvtErrNumTot", "RocErrNumTot"])
    print("--------------------")
    # format data
    cooked_data = format_data(raw_data)
    # get counts
    #fed_counts = get_counts(cooked_data)
    
    #return render_template('display_fed_data.html', fed_counts=fed_counts, fed_data=cooked_data)
    return render_template('display_fed_data.html', fed_data=cooked_data)

if __name__ == '__main__':
    app.run(debug=True)

