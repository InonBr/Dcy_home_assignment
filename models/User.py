from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()


class User(db.Model):
    user_id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    blogs = db.relationship('Blog', backref='owner', lazy=True)
    likes = db.relationship('BlogLikeByUser', backref='user', lazy=True)

