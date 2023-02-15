from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return 'Index page'

@app.route("/hello")
def hello():
    return 'Hello, World!'

@app.route("/<name>")
def hello_world(name):
    return f"Hello, {escape(name)}"

