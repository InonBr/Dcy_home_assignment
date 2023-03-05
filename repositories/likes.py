from models import BlogLikeByUser, Blog


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
