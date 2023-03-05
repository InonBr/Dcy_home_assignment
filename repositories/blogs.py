from models import Blog
from sqlalchemy import text
from sqlalchemy.orm import selectinload
import uuid


def create_new_blog(blog_text, current_user, session):
    new_blog_id = uuid.uuid4().hex

    new_blog = Blog(
        blog_id=new_blog_id,
        blog_owner_id=current_user["user_id"],
        blog_content=blog_text
    )

    session.add(new_blog)
    session.commit()

    return new_blog


def get_blog_by_id(blog_id, session):
    return session.query(Blog).filter(text("blog_id = :blog_id")).params(blog_id=blog_id).first()


def get_all_blogs():
    blogs = Blog.query.all()

    return [
        {
            "blog_id": blog.blog_id,
            "blog_owner_id": blog.blog_owner_id,
            "blog_content": blog.blog_content,
            "timestamp": blog.timestamp,
            "likes": [like.user_id for like in blog.likes]
        }
        for blog in blogs
    ]
