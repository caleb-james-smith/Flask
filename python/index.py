# index.py

from flask import Flask, render_template
app = Flask(__name__)

# # example: returning html directly
# @app.route('/')
# def index():
#     return '<html><body><h1>Hello World</h1></body></html>'

# example: use html file
#@app.route('/')
#def index():
#    return render_template('hello.html')

# example: use html file and pass variable
@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name=user)

# example: conditional statements in html
@app.route('/grade/<int:score>')
def grade(score):
    return render_template('grade.html', marks=score)

# example: for loop in html
@app.route('/result')
def result():
    scores = {'physics' : 80, 'chemistry' : 70, 'biology' : 60}
    return render_template('result.html', result=scores)

if __name__ == '__main__':
    app.run(debug=True)


