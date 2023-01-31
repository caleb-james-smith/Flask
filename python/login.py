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
        user = request.form['name']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user))

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


