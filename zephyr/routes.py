om zephyr import app
from flask import render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField


@app.route('/')
@app.route('/home')
def home_page():
    social_links = {
        "twitter": "https://x.com/oyematth",
        "linkedin": "https://www.linkedin.com/in/matthew-oyelami-1223b5244/",
        "github": "https://github.com/Oyematth01",
        "instagram": "https://www.instagram.com/oyematth/",
        "medium": "https://medium.com/@oyematth"
    }
    form = BookingForm()
    if form.validate_on_submit():
        # Redirect to a new page after the form is submitted
        return redirect(url_for('booking_page'))
    return render_template('home.html', social_links=social_links, form=form)

@app.route('/booking')
def booking_page():
    return "Welcome to the booking page!"

# @app.route('/zephyr')
# def market_page():
#     items = Item.query.all()
#     return render_template('market.html', items=items)