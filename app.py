from crypt import methods
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route("/message", methods=["POST"])
def form_post():
    if request.method == "POST":
        name = request.form.get("name")
    return render_template("message.html", name=name)


@app.route("/about")
def about():
    return "<h1>This is a Flask web application.</h1>"


if __name__ == "__main__":
    app.run(debug=True)  # TODO: set dbug=False before deployment!
