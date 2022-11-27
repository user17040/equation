from flask import Flask, render_template

from calculator import *


app = Flask(__name__)

@app.route("/<expr>")
def calculate(expr):
    return render_template("calculator_result.html",a=equation_solver(expr))


app.run()
