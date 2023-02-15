# static.py

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def static_example():
    return render_template("static_example.html")

if __name__ == '__main__':
   app.run(debug = True)

