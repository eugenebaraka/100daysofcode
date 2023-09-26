import requests
from flask import Flask, render_template


app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/<blog_id>')
def blog_post(blog_id):

    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
