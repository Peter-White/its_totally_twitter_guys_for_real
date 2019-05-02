from app import app, db, login
from flask import render_template, url_for, redirect, flash
from app.forms import TitleForm, LoginForm, RegisterForm, ContactForm, PostForm
from app.models import Title, Contact, Post, User
from flask_login import current_user, login_user, logout_user

@app.route('/')
@app.route('/index')
def index(header=''):
    products = [
        {
            'id': 1001,
            'pic': 'https://placehold.it/250x250',
            'title': 'Soap',
            'price': 3.98,
            'desc': 'Very clean soapy soap, descriptive text'
        },
        {
            'id': 1002,
            'pic': 'https://placehold.it/250x250',
            'title': 'Grapes',
            'price': 4.56,
            'desc': 'A bundle of grapey grapes, yummy'
        },
        {
            'id': 1003,
            'pic': 'https://placehold.it/250x250',
            'title': 'Pickles',
            'price': 5.67,
            'desc': 'A jar of pickles is pickly'
        },
        {
            'id': 1004,
            'pic': 'https://pixel.nymag.com/imgs/daily/vulture/2016/05/23/game-of-thrones-ep-5/23-got-ep-5-002.w700.h700.jpg',
            'title': 'HODOR',
            'price': 69.69,
            'desc': 'HODOR'
        },
        {
            'id': 1005,
            'pic': 'https://placehold.it/250x250',
            'title': 'Juice',
            'price': 2.68,
            'desc': 'Yummy orange juice'
        },
    ]

    header = Title.query.get(1).title

    return render_template('index.html', title="Home", products=products, header=header)

@app.route('/title', methods=['GET', 'POST'])
def title():
    form = TitleForm()

    print(form.title.data)
    if form.validate_on_submit():
        header = form.title.data

        data = Title.query.get(1)
        data.title = header

        # add to session and commit
        db.session.add(data)
        db.session.commit()

        flash(f'You have changed the title to {header}')
        return redirect(url_for('index'))

    return render_template('form.html', title='Change Title', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # if user is already logged in , send them to the profile page
    if current_user.is_authenticated:
        flash("You are already logged in!")
        return redirect(url_for('profile', username=username))

    if form.validate_on_submit():
        # query the database for the user trying to log in
        user = User.query.filter_by(email=form.email.data).first()

        # if user doesn't exist, reload the page and flash message
        # or if the password dosen't match the password stored
        if user is None or not user.check_password(form.password.data):
            flash('Credentials are incorrect.')
            return redirect(url_for('index'))

        # if user does exist, and credentials are correct, log then in and send them to their profile page
        login_user(user, remember = form.remember_me.data)
        flash("You are now logged in!")
        return redirect(url_for('profile', username=user.username))

    return render_template('form.html', title="Login", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    # check to see if the user is already logged in, if so send to index
    if current_user.is_authenticated:
        flask('You are already registered')
        return redirect(url_for('index'))

    if form.validate_on_submit():
        user = User(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            username = form.username.data,
            email = form.email.data,
            age = form.age.data,
            bio = form.bio.data,
            url = form.url.data
        )

        # call set password to create hash
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash(f'Thanks for registering, an email confirmation has been sent to {form.email.data}.')
        return redirect(url_for('login'))

    return render_template('form.html', title="Register", form=form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        try:
            contact = Contact(
                name = form.name.data,
                email = form.email.data,
                message = form.message.data
            )

            db.session.add(contact)
            db.session.commit()

            flash(f'Thanks for your submission, we will contact you shortly. A copy has been sent to {form.email.data}.')
            return redirect(url_for('index'))
        except:
            flash("Sorry your submission did not go through. Try again.")
            return redirect(url_for('contact'))

    return render_template('form.html', form=form, title="Contact Us")

@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username=""):
    form = PostForm()

    # posts = Post.query.all()

    user = User.query.filter_by(username=username).first()

    if form.validate_on_submit():
        try:
            tweet = Post(tweet=form.tweet.data, user_id=user.id)

            db.session.add(tweet)
            db.session.commit()

            return redirect(url_for('profile', username=username))
        except:
            flash("Broked")
            return redirect(url_for('profile'))

    return render_template('profile.html', title='Profile', form=form, user=user)

@app.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out!")
    return redirect(url_for('login'))
