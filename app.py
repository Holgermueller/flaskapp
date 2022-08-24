from flask import Flask, send_from_directory, request
import random
import string

app = Flask(__name__)


@app.route("/", methods=['GET'], ['POST'])
def base():
    return send_from_directory('client/public', 'index.html')
    if request

@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)



if __name__ == "__main__":
    app.run(debug=True)