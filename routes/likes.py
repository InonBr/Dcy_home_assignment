from flask import Blueprint, request, abort
from validators import BlogIdParamsValidators
from utils import auth_required, validate_request_params
from db.new_mysql_session import session
from repositories import get_user_by_email, get_blog_by_id, create_a_like, get_likes_based_on_blog_id, \
    find_like_and_delete

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

        current_like_list = get_likes_based_on_blog_id(blog_id)

        if current_user["user_id"] not in current_like_list:
            create_a_like(blog_id, current_user["user_id"], session)
            current_like_list.append(current_user["user_id"])
        else:
            find_like_and_delete(blog_id, current_user["user_id"], session)
            current_like_list.remove(current_user["user_id"])

        blog_dic = {
            "blog_id": blog_data.blog_id,
            "blog_owner_id": blog_data.blog_owner_id,
            "blog_content": blog_data.blog_content,
            "timestamp": blog_data.timestamp,
            "likes": current_like_list
        }

        return {"blog": blog_dic}, 201
    except Exception as e:
        session.rollback()

        print(str(e))

        return abort(500, 'Internal server error')
    finally:
        session.close()
