from flask import Blueprint, request, abort
from validators import BlogIdParamsValidators
from utils import auth_required, validate_request_params
from db.new_mysql_session import session
from repositories import get_user_by_email, get_blog_by_id, create_a_like, get_likes_based_on_blog_id

likes_bp = Blueprint('likes_api', __name__, url_prefix='/api')


@likes_bp.route('/like/<string:blog_id>', methods=["POST"])
@validate_request_params(BlogIdParamsValidators)
@auth_required
def like(blog_id):
    try:
        current_user = request.current_user

        user_data = get_user_by_email(current_user["email"], session)
        blog_data = get_blog_by_id(blog_id, session)

        if not user_data or not blog_data:
            return "blog or user not found", 404

        create_a_like(blog_id, current_user["user_id"], session)
        likes_list = get_likes_based_on_blog_id(blog_id)

        blog_dic = {
            "blog_id": blog_data.blog_id,
            "blog_owner_id": blog_data.blog_owner_id,
            "blog_content": blog_data.blog_content,
            "timestamp": blog_data.timestamp,
            "likes": likes_list
        }

        session.close()

        return {"blog": blog_dic}, 201
    except Exception as e:
        session.rollback()
        session.close()

        print(str(e))

        if "Duplicate entry" in str(e):
            return {"error": "user already liked this post"}, 400

        return abort(500, 'Internal server error')
