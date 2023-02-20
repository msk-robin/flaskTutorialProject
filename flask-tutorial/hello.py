from flask import Flask
from flask import url_for
from flask import request
from flask import render_template

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


# @app.route('/login',methods=['GET','POST'])
# def login2():
#     if request.method == 'POST':
#         return do_the_login()
    
#     else:  
#         return show_the_login_form()

        #flask provides a shortcut for decorating such routes with get(),post() all common HTTP methods.

# @app.get('/login')
# def login2_get():
#     return show_the_login_form()

# @app.get('/login')
# def login2_post():
#     return do_the_login()    
 
# Static Files
   #where the CSS and Javascript files come in place.    
#    To generate urls for static files use a 'special' endpiont name:
#     url_for('static',filename=''style.css')
#  
# he file has to be stored on the filesystem as static/style.css.


#rendering a template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name= None):
    return render_template("hello.html",name = name)