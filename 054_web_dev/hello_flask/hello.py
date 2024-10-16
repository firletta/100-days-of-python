from flask import Flask
from decorators import make_bold, make_emphasis, make_underlined
app = Flask(__name__)


@app.route("/")
@make_emphasis
@make_bold
@make_underlined
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<p>Goodbye, World!</p>"

@app.route("/<name>")
@make_emphasis
@make_bold
@make_underlined
def hello(name):
    return f"<p>Hello, {name}!</p>"

if __name__ == "__main__":
    app.run(debug=True)