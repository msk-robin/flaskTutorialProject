from flask import Flask
from flask import url_for

app = Flask(__name__)

# @app.route("/")

# def hello_world():
#     return "<h1>Am msk_robin, Learning flask is fun!</h1>"


@app.route("/projects/")
def projects():
    return "The project page"

@app.route('/about')
def about():
    return 'The about page'    


# learning URL Building  { url_for()  }
@app.route('/')
def index():
    return 'index'   

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile (username):
    username = "kendy"
    return f'{username}\'s profile'
