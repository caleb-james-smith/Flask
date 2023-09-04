# display_fed_data.py

import tools
import datetime
from flask import Flask, render_template

app = Flask(__name__)

# Display FED data from input json file.

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
    #input_file  = "data/fed_data.json"
    input_file  = "data/FEDMonitor_2023_09_01_v2.json"
    # load data from json file
    raw_data    = tools.load_data(input_file)
    # print data
    tools.print_key_depth(raw_data)
    # format data
    cooked_data = format_data(raw_data)
    # get counts
    #fed_counts = get_counts(cooked_data)
    
    #return render_template('display_fed_data.html', fed_counts=fed_counts, fed_data=cooked_data)
    return render_template('display_fed_data.html', fed_data=cooked_data)

if __name__ == '__main__':
    app.run(debug=True)

