from flask import Flask

app = Flask(__name__)

@app.route("/")
def slash():
    return """<p>Hello App</p>"""


@app.route("/hello")
def hello():
    return """<p>Hello, World</p>"""