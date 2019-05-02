from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import TitleForm, LoginForm, RegisterForm, ContactForm
from app.models import Title, Contact

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

    if form.validate_on_submit():
        flash(f'E-Mail: {form.email.data} \t Password: {form.password.data}')
        return redirect(url_for('index'))

    return render_template('form.html', title="Login", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
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

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html', title='Profile')
