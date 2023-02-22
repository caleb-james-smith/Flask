# student.py

from flask import Flask, render_template, request
app = Flask(__name__)

# for values in dictionary, 
# change non-negative integers from string to int;
# only works non-negative integers (n >= 0)
def format_result(result):
    new_result = {}
    for key in result:
        value = result[key]
        # only true for strings that are non-negative integers (n >= 0)
        if value.isdigit():
            new_result[key] = int(value)
        else:
            new_result[key] = value
    return new_result

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    debug = False
    if request.method == 'POST':
        # dictionary from html form
        result = request.form
        # change numbers from string to int
        new_result = format_result(result)
        # print keys, values, and value types to debug
        if debug:
            for key in new_result:
                value = new_result[key]
                print("key: {0}, value: {1}, value type: {2}".format(key, value, type(value)))
        return render_template('result.html', result=new_result)

if __name__ == '__main__':
    app.run(debug=True)

