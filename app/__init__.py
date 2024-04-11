from flask import Flask,request
from flask import render_template,url_for, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "perform login"
    else:
        return "return login form in html"
    

#uses get/post instead of "route"
@app.get('/signup')
def signup_get():
    return "send the signup form"

#sepration of concern, for cleanliness ig
@app.post('/signup')
def signup_post():
    return "perform signup action in the backend"
