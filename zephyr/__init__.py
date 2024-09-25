from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '8a8f900d1be43b891b7703d6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zephyr.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "sign_in_page"
login_manager.login_message_category= "info"

from zephyr import routes

with app.app_context():
    db.create_all()