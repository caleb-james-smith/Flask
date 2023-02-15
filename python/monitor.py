# monitor.py

import json
import datetime
from flask import Flask, render_template

app = Flask(__name__)

# Simple and basic example FED monitoring page.

now         = datetime.datetime.now()
time_stamp  = now.strftime('%Y-%m-%d %H:%M:%S')

# example data
feds = [
    {"name" : "FED_1000", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1001", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1002", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1003", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1004", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 1},
    {"name" : "FED_1005", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 1},
    {"name" : "FED_1006", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1007", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1008", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1009", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1010", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1011", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 1},
    {"name" : "FED_1012", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1013", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1014", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1015", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1016", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1017", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 1},
    {"name" : "FED_1018", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1019", "time" : time_stamp, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
]

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

