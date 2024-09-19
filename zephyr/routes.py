from zephyr import app, db
from flask import render_template, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from zephyr.forms import RegisterForm, LoginForm, BookingForm, ConfirmBookingForm
from zephyr.models import User, Booking
from flask_login import login_user, logout_user, login_required


social_links = {
        "twitter": "https://x.com/oyematth",
        "linkedin": "https://www.linkedin.com/in/matthew-oyelami-1223b5244/",
        "github": "https://github.com/Oyematth01",
        "instagram": "https://www.instagram.com/oyematth/",
        "medium": "https://medium.com/@oyematth"
}

@app.route('/')
@app.route('/home')
def home_page():
    form = BookingForm()
    return render_template('home.html', social_links=social_links, form=form)

@app.route('/Sign_Up', methods=['GET', 'POST'])
def sign_up_page():
    form = RegisterForm()
    if form.validate_on_submit():
        # This is to check if user already exists
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already exists.', 'danger')
            return redirect(url_for('sign_up_page'))
        
        #This is to create a new user
        user_to_create = User(name=form.name.data,
                              username=form.username.data,
                              email=form.email.data,
                              password=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()                
        return redirect(url_for('sign_in_page'))
    
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There  was an error  with creating an account: {err_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route('/Sign_In', methods=['GET', 'POST'])
def sign_in_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email=form.email.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('dashboard'))
        else:
            flash('Username and password do not match, try again', category='danger')

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




@app.route('/dashboard')
@login_required
def dashboard():
    items = Booking.query.all()
    return render_template('dashboard.html', items=items, social_links=social_links)

@app.route('/logout')
def logout_Page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))