# monitor.py

from flask import Flask, render_template
app = Flask(__name__)

# Simple and basic example FED monitoring page.

# use html template with conditional statements and loops
@app.route('/monitor')
def result():
    # example FED status codes
    feds = {
        'FED_1000' : 0,
        'FED_1001' : 0,
        'FED_1002' : 1,
        'FED_1003' : 1,
        'FED_1004' : 0,
        'FED_1005' : 0,
        'FED_1006' : 0,
        'FED_1007' : 0,
        'FED_1008' : 1,
        'FED_1009' : 0,
    }
    return render_template('monitor.html', result=feds)

if __name__ == '__main__':
    app.run(debug=True)


