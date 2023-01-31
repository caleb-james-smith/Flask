# login.py

from flask import Flask, redirect, url_for, request

# Login Flask example

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s.' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print(" - request method: {0}".format(request.method))
        user = request.form['name']
        return redirect(url_for('success', name=user))
    elif request.method == 'GET':
        print(" - request method: {0}".format(request.method))
        user = request.args.get('name')
        return redirect(url_for('success', name=user))
    else:
        print("ERROR: The request method '{0}' is not supported.".format(request.method))
        return

if __name__ == '__main__':
    app.run(debug=True)

# ------------------------
# How to Run
#
# First, start the server:
# python python/login.py 
#
# Then, open this file path in a browser:
# /Users/caleb/Code/Flask/index/login.html
#
# Enter a name and click submit.
#
# ------------------------


