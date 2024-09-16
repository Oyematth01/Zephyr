from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, IntegerField, DateField, EmailField, SelectField, SubmitField, BooleanField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, NumberRange
# from zephyr.models import User



class RegisterForm(FlaskForm):
    # def validate_username(self, username_to_check):
    #     user = User.query.filter_by(username=username_to_check.data).first()
    #     if user:
    #         raise ValidationError('Username already exists! Please try a different username')

    # def validate_email(self, email_address_to_check):
    #     email = User.query.filter_by(email=email_address_to_check.data).first()
    #     if email:
    #         raise ValidationError('Email Address already exists! Please try a different email address')


    name = StringField(label='Full Name:', validators=[DataRequired()])
    username = StringField(label='User Name:', validators=[Length(min=2, max=20), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label='Confirm Password:', validators=[EqualTo('password'), DataRequired()])
    terms = BooleanField('Agree with our')
    submit = SubmitField(label='Create Account')



class LoginForm(FlaskForm):
    email = EmailField(label='Email Address:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    login = SubmitField('Log In')



class BookingForm(FlaskForm):
    check_in = DateField(label='Arrival Date', validators=[DataRequired()])
    check_out = DateField(label='Departure Date', validators=[DataRequired()])
    adults = IntegerField(label='Adults', validators=[DataRequired(), NumberRange(min=0, max=6)])
    children = IntegerField(label='Children', validators=[DataRequired(), NumberRange(min=0, max=6)])
    room_type = SelectField(label='Room Type', choices=[('Single Room', 'Single Room'), ('Single Deluxe Room', 'Single Deluxe Room'), 
                                                        ('Double Deluxe Room', 'Double Deluxe Room'), 
                                                        ('Honeymoon Suite', 'Honeymoon Suite'), 
                                                        ('Villa Room', 'Villa Room'), ('Executive Room', 'Executive Room'), 
                                                        ('Triple Room', 'Triple Room'), ('Bridal Suite', 'Bridal Suite'), 
                                                        ('Standard Suite Room', 'Standard Suite Room'), ('King Room', 'King Room'), 
                                                        ('Queen Room', 'Queen Room'), ('Duplex Room', 'Duplex Room')]
                            )
    book_now = SubmitField("Book Now!")


class ConfirmBookingForm(FlaskForm):
    name = StringField(label='Enter your Full Name', validators=[DataRequired(), Length(min=5, max=60)], unique=True)
    Email = EmailField(label='Email Address:', validators=[Email(), DataRequired()], unique=True)
    Occupation = StringField(label=' Enter your Occupation', validators=[DataRequired()])