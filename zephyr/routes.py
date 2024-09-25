from zephyr import app, db
from flask import render_template, redirect, url_for, flash, session, request
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from zephyr.forms import RegisterForm, LoginForm, BookingForm, Confirm_Booking_Form
from zephyr.models import User, Booking
from flask_login import login_user, logout_user, login_required
from datetime import datetime

social_links = {
        "twitter": "https://x.com/oyematth",
        "linkedin": "https://www.linkedin.com/in/matthew-oyelami-1223b5244/",
        "github": "https://github.com/Oyematth01",
        "instagram": "https://www.instagram.com/oyematth/",
        "medium": "https://medium.com/@oyematth"
}

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home_page():
    form = BookingForm()
    if form.validate_on_submit():
        # Save booking form data to session
        session['check_in'] = form.check_in.data
        session['check_out'] = form.check_out.data
        session['adults'] = form.adults.data
        session['children'] = form.children.data
        session['room_type'] = form.room_type.data
        return redirect(url_for('confirm_booking_page'))
    else:
        print(form.errors)
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


@app.route('/confirm_booking', methods=['GET', 'POST'])
def confirm_booking_page():
    form = Confirm_Booking_Form()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        check_in_time = form.check_in_time.data
        check_out_time = form.check_out_time.data

        flash('You have successfully book a room, login to see your dashboard', category='success')
        return redirect(url_for("home_page"))
    
    if request.method == 'GET':
        # This is use to Pre-fill the form with session data
        # Retrieving the date from session, which is a string, and converting it to a datetime object
        check_in_str = session.get('check_in')
        if check_in_str:
            form.check_in.data = datetime.strptime(check_in_str, "%a, %d %b %Y %H:%M:%S %Z")  # Assuming the date format is "YYYY-MM-DD"
        check_out_str = session.get('check_out')
        if check_out_str:
            form.check_out.data = datetime.strptime(check_out_str, "%a, %d %b %Y %H:%M:%S %Z")
    
        form.adults.data = session.get('adults')
        form.children.data = session.get('children')
        form.room_type.data = session.get('room_type')
    return render_template('confirm_booking.html', social_links=social_links, form=form)





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