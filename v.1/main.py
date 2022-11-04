from flask import Flask, render_template
import requests

blogs_api = "https://api.npoint.io/10a04cb38ca95cf9e01a"

app = Flask(__name__)

response = requests.get(url=blogs_api)
all_blogs = response.json()

@app.route('/')
def home():
    return render_template("index.html", blogs = all_blogs)

@app.route("/post/<int:id>") 
def blog(id):
    blog_id = id
    return render_template("post.html", blogs= all_blogs, post_id = blog_id)

if __name__ == "__main__":
    app.run(debug=True)
