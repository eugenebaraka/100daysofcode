from flask import Flask


def make_bold(function):
    def wrapper():
        f"""<b>{function()}</b>"""
    return wrapper


app = Flask(__name__)


@app.route("/")
@make_bold
def hello_world():
    return "<p>Hello world</p>"


hello_world()


if __name__ == "__main__":
    app.run(debug=True)

