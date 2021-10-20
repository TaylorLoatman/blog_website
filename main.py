from flask import Flask, render_template
import requests


app = Flask(__name__)
all_post = requests.get(url='https://api.npoint.io/5f05c60ffd6c5a8df6c0').json()


@app.route('/')
def home():
    return render_template("index.html", blog_post=all_post)


@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    return render_template('post.html', blog_id=blog_id, blog_post=all_post)


if __name__ == "__main__":
    app.run(debug=True)
