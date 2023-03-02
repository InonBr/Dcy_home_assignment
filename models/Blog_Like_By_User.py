from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BlogLikeByUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.String(36), db.ForeignKey('blog.blog_id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.user_id'), nullable=False)
    __table_args__ = (db.UniqueConstraint('blog_id', 'user_id', name='_blog_user_uc'),)
