# monitor.py

import json
import datetime
from flask import Flask, render_template

app = Flask(__name__)

# Simple and basic example FED monitoring page.

# load data from input json file
def load_data(input_file):
    with open(input_file, "r") as f:
        data = json.load(f)
    return data

# format data as a sorted list of dictionaries
def format_data(input_data):
    output_data = []
    # sort keys: make sure to use list() so that sort() works!
    keys = list(input_data.keys())
    keys.sort()
    for key in keys:
        output_data.append(input_data[key])
    return output_data

# use html template with conditional statements and loops
@app.route('/monitor')
def result():
    # input json file with data
    input_file  = "data/fed_data.json"
    # load data from json file
    raw_data    = load_data(input_file)
    # format data
    cooked_data = format_data(raw_data)
    
    return render_template('monitor.html', feds=cooked_data)

if __name__ == '__main__':
    app.run(debug=True)

