"""Models for Blogly."""
from email.policy import default
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG_URL = "https://blog.nscsports.org/default-img/"

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """Registered Users"""

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.Text(20),
                           nullable=False)

    last_name = db.Column(db.Text(20),
                          nullable=False)

    img_url = db.Column(db.Text(),
                        nullable=False,
                        default=DEFAULT_IMG_URL)

def connect_db(app):
    db.app = app
    db.init_app(app)