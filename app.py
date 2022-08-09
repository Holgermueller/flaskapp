from urllib import request
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_data_from_form():
    if request.method == 'POST':
        result = request.form
        return render_template('index.html', result=result)



if __name__ == "__main__":
    app.run()