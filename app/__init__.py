from flask import Flask,request
from flask import render_template,url_for, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.get('/profile')
def profile():
    name = "demon"
    age = 21
    pets=['zo', 'azakaban', 'voldi', 'banana','pancake']
    return render_template('profile.html', name=name, age=age, pets=pets )
