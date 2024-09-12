from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



app = Flask(__name__)
app.config['SECRET_KEY'] = '8a8f900d1be43b891b7703d6'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from zephyr import routes