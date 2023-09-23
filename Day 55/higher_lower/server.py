import random

from flask import Flask


app = Flask(__name__)


@app.route("/")
def home_page():
    return "<h1>Guess a number between 0 and 9</h1>"


@app.route("/<num>")
def number_guessing(num):
    random_num = random.choice(range(0, 1))
    if int(num) == random_num:
        return "<h1>You've got it right</h1>" \
               "<img src='https://media.giphy.com/media/ND6xkVPaj8tHO/giphy.gif'/>"
    else:
        return "<h1>Try again!!</h1>" \
               "<img src='https://media.giphy.com/media/aHzTN9LY8msQx9oweY/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
