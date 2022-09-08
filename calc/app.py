from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_page():
    a = int(request.args["a"])
    b = int(request.args["b"])
    c = str(add(a, b))
    return c

@app.route("/sub")
def sub_page():
    a = int(request.args["a"])
    b = int(request.args["b"])
    c = str(sub(a, b))
    return c

@app.route("/mult")
def mult_page():
    a = int(request.args["a"])
    b = int(request.args["b"])
    c = str(mult(a, b))
    return c

@app.route("/div")
def div_page():
    a = int(request.args["a"])
    b = int(request.args["b"])
    c = str(div(a, b))
    return c

OPERATIONS = {"add": add, "sub": sub, "mult": mult, "div": div}

@app.route("/math/<operation>")
def all_page(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    c = str(OPERATIONS[operation](a, b))
    return c
