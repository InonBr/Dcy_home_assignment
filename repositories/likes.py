from models import BlogLikeByUser, Blog
from sqlalchemy import text


def create_a_like(blog_id, user_id, session):
    like = BlogLikeByUser(blog_id=blog_id, user_id=user_id)

    session.add(like)
    session.commit()


def get_likes_based_on_blog_id(blog_id):
    likes = (
        BlogLikeByUser.query
        .join(Blog)
        .filter(Blog.blog_id == blog_id)
        .all()
    )

    return [like.user_id for like in likes]


def find_like_and_delete(blog_id, user_id, session):
    like = session.query(BlogLikeByUser).filter(text("user_id = :user_id AND blog_id = :blog_id")).params(
        user_id=user_id, blog_id=blog_id).one()

    session.delete(like)
    session.commit()
