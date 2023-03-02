from db.database import sql_alchemy_db


class BlogLikeByUser(sql_alchemy_db.Model):
    id = sql_alchemy_db.Column(sql_alchemy_db.Integer, primary_key=True)
    blog_id = sql_alchemy_db.Column(sql_alchemy_db.String(36), sql_alchemy_db.ForeignKey('blog.blog_id'),
                                    nullable=False)
    user_id = sql_alchemy_db.Column(sql_alchemy_db.String(36), sql_alchemy_db.ForeignKey('user.user_id'),
                                    nullable=False)
    __table_args__ = (sql_alchemy_db.UniqueConstraint('blog_id', 'user_id', name='_blog_user_uc'),)
