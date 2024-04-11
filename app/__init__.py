from flask import request, Flask

app = Flask(__name__)



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