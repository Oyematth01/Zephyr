from zephyr import app
from flask import render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField


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
        return redirect(url_for('confirm_booking', name=form.name.data, email=form.email.data, room_number=form.room_number.data))
    return render_template('home.html', confirm_booking.html, social_links=social_links, form=form)

@app.route('/booking')
def booking_page():
    return "Welcome to the booking page!"


@app.route('/confirm_booking', methods=['GET', 'POST'])
def confirm_booking():
    # Initialize ConfirmBookingForm with data from the URL parameters
    form = ConfirmBookingForm(request.args)
    if form.validate_on_submit():
        # Process the confirmed booking here
        return redirect(url_for('booking_complete'))
    return render_template('confirm_booking.html', form=form)

@app.route('/booking_complete')
def booking_complete():
    return "Booking Confirmed!"

# @app.route('/zephyr')
# def market_page():
#     items = Item.query.all()
#     return render_template('market.html', items=items)


