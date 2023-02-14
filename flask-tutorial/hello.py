from flask import Flask
from flask import url_for
from flask import request


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
    # username = "kendy"
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('index'))
    print(url_for('login', next='/'))
    print(url_for('profile',username='msk robin'))


# HTTP Methods 
# route() method decorator  helps in handling diffrent HTTPS methods


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    
    else:  
        return show_the_login_form()

        #flask provides a shortcut for decorating such routes with get(),post() all common HTTP methods.

@app.get('/login')
def login_get():
    return show_the_login_form()

@app.get('/login')
def login_post():
    return do_the_login()    
 
# Static Files
           