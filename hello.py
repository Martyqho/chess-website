from flask import render_template
from flask import Flask
app = Flask(__name__)
from markupsafe import escape

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hi')
def hi_world():
    return 'Hi, World!'

@app.route('/user/<username>')
def user_profile(username):
    return render_template("user_profile.html", username=username)
