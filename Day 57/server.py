from flask import Flask, render_template
import datetime as dt
import requests

AGIFY_ENDPOINT = "https://api.agify.io/"
GENDERIZE_ENDPOINT = "https://api.genderize.io/"


app = Flask(__name__)


@app.route("/")
def hello():
    year = dt.datetime.now().year
    return render_template("index.html", year=year)


@app.route("/guess/<name>")
def age_gender(name: str):
    params = {"name": name}
    response_age = requests.get(url=AGIFY_ENDPOINT, params=params)
    age = response_age.json()["age"]
    response_gender = requests.get(url=GENDERIZE_ENDPOINT, params=params)
    gender = response_gender.json()["gender"]

    year = dt.datetime.now().year

    return render_template("index.html", name=name.capitalize(), age=age, gender=gender, year=year)


@app.route("/blog")
def get_blog():
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()

    return render_template("index.html", all_posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
