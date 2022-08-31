"""Models for Blogly."""
import datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy, func

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


class Post(db.Model):
    """User Posts"""

    __tablename__ = 'posts'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    title = db.Column(db.Text(100),
                      nullable=False)

    content = db.Column(db.String,
                        nullable=False)

    created_at = db.Column(db.DateTime,
                           nullable=False,
                           default=datetime.datetime.now)

    user_code = db.Column(db.Text, db.ForeignKey('users.id'))