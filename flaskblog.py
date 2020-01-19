from flask import Flask, render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '880a5749fd55dd513da415e34c46b500'

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


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
