from zephyr import db
from zephyr import bcrypt
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.timezone.utc)
    bookings = db.relationship('Booking', backref='user', lazy=True)

    # Methods
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

class Booking(db.Model):
    __tablename__ = 'booking'  # Optional: explicitly set table name
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id = db.Column(db.Integer, nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.timezone.utc)

    # If you have a Room model, you can set up a relationship
    # room = db.relationship('Room', backref='bookings', lazy=True)