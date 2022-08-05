from crypt import methods
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "<h1>Welcome to the app</h1>", 200


if __name__ == "__main__":
    app.run(debug=True)  # TODO: set dbug=False before deployment!
