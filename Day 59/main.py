from flask import Flask, render_template
import requests

# get fake blogs
blogs = requests.get(url="https://api.npoint.io/a8a0ea30169ab24f150d").json()
# for blog in blogs:
#     print(blog)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/blog/<int:index>")
def get_post(index):
    requested_post = None
    for post in blogs:
        if post['id'] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True)

