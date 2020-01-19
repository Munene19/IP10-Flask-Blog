from datetime import datetime
from flask import Flask, render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '880a5749fd55dd513da415e34c46b500'
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    Email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.Email}', '{self.image_file}')

class Post(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.string(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False,  )

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')

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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account successfully created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Welcome {form.username.data}", 'success')
        return redirect(url_for('home'))
    else:
        flash("Login unsuccessfull. Please check credentials ", "danger")

    return render_template('login.html', title='login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
