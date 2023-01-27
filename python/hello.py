# hello.py

from flask import Flask

# First Flask example

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    #app.run()
    #app.run(host="127.0.0.1", port="5000", debug=False)
    app.run(host="127.0.0.1", port="5555", debug=True)


