from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, IntegerField, DateField, EmailField, SelectField, SubmitField 
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class RegisterForm(FlaskForm):
    name = StringField(label='Full Name', validator=[DataRequired()])
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label='Confirm Password:', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class BookingForm(FlaskForm):
    checkin = IntegerField(label='Arrival Date', validators=[DataRequired()])
    checkout = IntegerField(label='Departure Date', validators=[DataRequired()])
    Adults = StringField(Label='Adults', validators=[DataRequired()])
    room_type = SelectField(label='Room Type', choices=[('Single Room', 'Single Room'), ('Single Deluxe Room', 'Single Deluxe Room'), 
                                                        ('Double Deluxe Room', 'Double Deluxe Room'), 
                                                        ('Honeymoon Suite', 'Honeymoon Suite'), 
                                                        ('Villa Room', 'Villa Room'), ('Executive Room', 'Executive Room'), 
                                                        ('Triple Room', 'Triple Room'), ('Bridal Suite', 'Bridal Suite'), 
                                                        ('Standard Suite Room', 'Standard Suite Room'), ('King Room', 'King Room'), 
                                                        ('Queen Room', 'Queen Room'), ('Duplex Room', 'Duplex Room')]
                            )