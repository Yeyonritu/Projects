from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()
posts = []

for post in all_posts:
    post_obj = Post(post["id"], post["subtitle"], post["title"], post["body"])
    posts.append(post_obj)
    
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts_obj = posts)

@app.route('/post/<int:index>')

def show_post(index):
    requested_post = ""
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
