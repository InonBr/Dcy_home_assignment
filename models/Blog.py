from datetime import datetime
from db.database import sql_alchemy_db
from sqlalchemy.orm import relationship, backref
import uuid


class Blog(sql_alchemy_db.Model):
    blog_id = sql_alchemy_db.Column(sql_alchemy_db.String(36), primary_key=True, default=str(uuid.uuid4()))
    blog_owner_id = sql_alchemy_db.Column(sql_alchemy_db.String(36), sql_alchemy_db.ForeignKey('user.user_id'),
                                          nullable=False)
    blog_content = sql_alchemy_db.Column(sql_alchemy_db.Text, nullable=False)
    timestamp = sql_alchemy_db.Column(sql_alchemy_db.DateTime, default=datetime.utcnow)
    likes = relationship('BlogLikeByUser', cascade='all, delete-orphan', backref=backref('blog', lazy=True))

