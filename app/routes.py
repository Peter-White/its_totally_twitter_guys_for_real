from app import app
from flask import render_template, url_for, redirect
from app.forms import TitleForm, LoginForm, RegisterForm, ContactForm
from app.parser import parse

@app.route('/')
@app.route('/index')
@app.route('/index/<header>', methods=['GET'])
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

    return render_template('index.html', title="Home", products=products, header=header)

@app.route('/title', methods=['GET', 'POST'])
def title():
    form = TitleForm()

    if form.validate_on_submit():
        header = form.title.data

        # call parser
        found = parse(header)

        if found:
            print("That is a name")

        return redirect(url_for('index', header=header))

    return render_template('form.html', title='Change Title', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print(f'E-Mail: {form.email.data} \t Password: {form.password.data}')
        return redirect(url_for('index'))

    return render_template('form.html', title="Login", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        print(f'First Name: {form.first_name.data} \t Last Name: {form.last_name.data} \t Username: {form.username.data} \t E-Mail: {form.email.data} \t Age: {form.age.data} \t Bio: {form.bio.data} \t Profile Pic URL: {form.url.data} \t Password: {form.password.data} \t Confirm Password: {form.password2.data}')
        return redirect(url_for('login'))

    return render_template('form.html', title="Register", form=form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        print(f'Name: {form.name.data} \t Email: {form.email.data} \t Message: {form.message.data}')
        return redirect(url_for('index'))

    return render_template('form.html', title="Contact", form=form)
