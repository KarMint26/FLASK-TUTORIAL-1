import numpy as np
from scipy.linalg import solve
from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/jacob")
def jacob():
    return render_template("jacob.html")