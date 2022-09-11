from flask import Flask, render_template
# import random
# import string

app = Flask(__name__)


@app.route("/", methods=['GET'])
def base():
    data = 'Button clicked'
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
