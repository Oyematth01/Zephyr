from zephyr import app
from flask import render_template, redirect, url_for, flash
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
    }
    form = BookingForm()
    return render_template('home.html', social_links=social_links, form=form), social_links

@app.route('/Sign_Up', methods=['GET', 'POST'])
def sign_up_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password=form.password.data)
        return redirect(url_for('sign_in_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There  was an error  with creating an account: {err_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route('/Sign_In')
def sign_in_page():
    form = LoginForm()
    return render_template('login.html', form=form)



@app.route('/Booking', methods=['GET', 'POST'])
def booking_page():
    social_links = home_page()
    form = BookingForm()
    if form.validate_on_submit():
        return redirect(url_for('confirm_booking', name=form.name.data, email=form.email.data, room_number=form.room_number.data))
    return render_template('bookingform.html', form=form, social_links=social_links)


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

