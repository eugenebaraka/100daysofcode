from flask import Flask, render_template
import requests
from post import Post

# get all posts
post_contents = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()

posts = []

for post in post_contents:
    obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    posts.append(obj)

print(posts[0].subtitle)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/blog/<int:index>")
def get_blog(index):
    selected_post = None
    for blogpost in posts:
        if blogpost.id == index:
            selected_post = blogpost
    return render_template("post.html", post=selected_post)


if __name__ == "__main__":
    app.run(debug=True)
