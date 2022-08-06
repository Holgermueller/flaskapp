from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

topbar = Navbar(
    View('About', 'get_about'),
    View('Form', 'get_form')
)

nav = Nav()
nav.register_element('top', topbar)

app = Flask(__name__)
Bootstrap(app)


@app.route("/message", methods=["GET", "POST"])
def get_form():
    return render_template('index.html')


# @app.route("/message", methods=["POST"])
# def form_post():
#     if request.method == "POST":
#         name = request.form.get("name")
#     return render_template("message.html", name=name)


@app.route("/about", methods=["GET"])
def get_about():
    return "<h1>This is a Flask web application.</h1>"


nav.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)  # TODO: set dbug=False before deployment!
