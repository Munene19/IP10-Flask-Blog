from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {'author': 'Mike',
     'title': 'first post',
     'content': 'first content',
     'date_posted': '1/1/2020'},

    {'author': 'james',
     'title': 'second post',
     'content': 'second content',
     'date_posted': '1/1/2020'}
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


if __name__ == "__main__":
    app.run(debug=True)
