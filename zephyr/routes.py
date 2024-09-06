from zephyr import app
from flask import render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField
from zephyr.forms import RegisterForm, LoginForm, BookingForm, ConfirmBookingForm


@app.route('/')
@app.route('/home')
def home_page():
    social_links = {
        "twitter": "https://x.com/oyematth",
        "linkedin": "https://www.linkedin.com/in/matthew-oyelami-1223b5244/",
        "github": "https://github.com/Oyematth01",
        "instagram": "https://www.instagram.com/oyematth/",
        "medium": "https://medium.com/@oyematth"
    return render_template('home.html', social_links=social_links)
    }


@app.route('/booking', methods=['GET', 'POST'])
def booking_page():
    form = BookingForm()
    if form.validate_on_submit():
        # Redirect to a new page after the form is submitted
        return redirect(url_for('confirm_booking', name=form.name.data, email=form.email.data, room_number=form.room_number.data))
    return render_template('confirm_booking.html', form=form)


@app.route('/confirm_booking', methods=['GET', 'POST'])
def confirm_booking():
    # Initialize ConfirmBookingForm with data from the URL parameters
    form = ConfirmBookingForm()
    if form.validate_on_submit():
        # Process the confirmed booking here
        return redirect(url_for('booking_complete'))
    return render_template('confirm_booking.html', form=form)

@app.route('/booking_complete')
def booking_complete():
    return "Booking Confirmed!"

