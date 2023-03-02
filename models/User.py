from db.database import sql_alchemy_db
from datetime import datetime
import uuid


class User(sql_alchemy_db.Model):
    user_id = sql_alchemy_db.Column(sql_alchemy_db.String(36), primary_key=True, default=str(uuid.uuid4()))
    first_name = sql_alchemy_db.Column(sql_alchemy_db.String(50), nullable=False)
    last_name = sql_alchemy_db.Column(sql_alchemy_db.String(50), nullable=False)
    email = sql_alchemy_db.Column(sql_alchemy_db.String(255), unique=True, nullable=False)
    password = sql_alchemy_db.Column(sql_alchemy_db.String(255), nullable=False)
    timestamp = sql_alchemy_db.Column(sql_alchemy_db.DateTime, default=datetime.utcnow)
    blogs = sql_alchemy_db.relationship('Blog', backref='owner', lazy=True)
    likes = sql_alchemy_db.relationship('BlogLikeByUser', backref='user', lazy=True)
