from distutils.debug import DEBUG
from flask import Flask, render_template, request, jsonify
import random
import string

DEBUG = True


app = Flask(__name__)
app.config.from_object(__name__)





@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

def passgen():
    password_length = request.form['length']
    has_numbers = request.form['numbers']
    has_special = request.form['special']


if __name__ == "__main__":
    app.run()