from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()


class Blog(db.Model):
    blog_id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    blog_owner_id = db.Column(db.String(36), db.ForeignKey('user.user_id'), nullable=False)
    blog_content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    likes = db.relationship('BlogLikeByUser', backref='blog', lazy=True)

