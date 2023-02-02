# monitor.py

import datetime
from flask import Flask, render_template

app = Flask(__name__)

# Simple and basic example FED monitoring page.

now = datetime.datetime.now()
now_string = now.strftime('%Y-%m-%d %H:%M:%S')

# data
feds = [
    {"name" : "FED_1000", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1001", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1002", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1003", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1004", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 1},
    {"name" : "FED_1005", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 1},
    {"name" : "FED_1006", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1007", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1008", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1009", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1010", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1011", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 1},
    {"name" : "FED_1012", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1013", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1014", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1015", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1016", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1017", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 1},
    {"name" : "FED_1018", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
    {"name" : "FED_1019", "time" : now_string, "happy_counter" : 10, "sad_counter" : 0, "middle_of_the_road_counter" : 5, "status_code" : 0},
]

# use html template with conditional statements and loops
@app.route('/monitor')
def result():
    # example FED status codes
    return render_template('monitor.html', feds=feds)

if __name__ == '__main__':
    app.run(debug=True)

