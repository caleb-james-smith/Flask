# hello.py

from flask import Flask, redirect, url_for

# First Flask example

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/int_example/<int:my_int>')
def show_int(my_int):
    return 'Your int is %d' % my_int

@app.route('/float_example/<float:my_float>')
def show_float(my_float):
    return 'Your float is %f' % my_float

@app.route('/admin')
def hello_admin():
    return 'Hello admin.'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s. You are a guest.' % guest

@app.route('/user/<user>')
def hello_user(user):
    if user == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=user))

app.add_url_rule('/', 'hello', hello_world)

if __name__ == '__main__':
    #app.run()
    #app.run(debug=True)
    app.run(host="127.0.0.1", port="5000", debug=True)
    #app.run(host="127.0.0.1", port="5001", debug=True)
    #app.run(host="127.0.0.1", port="5555", debug=True)

# Example URLs:
# - http://127.0.0.1:5000
# - http://127.0.0.1:5000/hello
# - http://127.0.0.1:5000/hello/Caleb
# - http://127.0.0.1:5000/guest/Bilbo
# - http://127.0.0.1:5000/user/admin
# - http://127.0.0.1:5000/user/Bilbo



