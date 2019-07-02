from flask import Flask, render_template, make_response
from jinja2 import Template

app = Flask(__name__)



@app.route('/')
@app.route('/index', methods=["GET"])
def index():
    return render_template('Nemo.html')