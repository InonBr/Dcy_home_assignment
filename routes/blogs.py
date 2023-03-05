from flask import Blueprint, request, abort
from validators import NewBlogValidator, BlogIdParamsValidators
from utils import validate_request_body, auth_required, validate_request_params
from db.new_mysql_session import session
from repositories import get_user_by_email, create_new_blog, get_all_blogs, get_blog_by_id_and_user_id, \
    delete_current_blog

blogs_bp = Blueprint('blogs_api', __name__, url_prefix='/api')


@blogs_bp.route('/get_blogs', methods=["GET"])
@auth_required
def get_blogs():
    try:
        current_user = request.current_user

        user_data = get_user_by_email(current_user["email"], session)

        if not user_data:
            return "user not found", 404

        blogs = get_all_blogs()

        return {"new_blog": blogs}, 200
    except Exception as e:
        session.rollback()

        print(str(e))

        return abort(500, 'Internal server error')
    finally:
        session.close()


@blogs_bp.route('/new_blog', methods=["POST"])
@validate_request_body(NewBlogValidator)
@auth_required
def new_post():
    try:
        current_user = request.current_user
        blog_text = request.json["blog_text"]

        user_data = get_user_by_email(current_user["email"], session)

        if not user_data:
            return "user not found", 404

        new_blog_data = create_new_blog(blog_text, current_user, session)

        blog_dic = {
            "blog_id": new_blog_data.blog_id,
            "blog_owner_id": new_blog_data.blog_owner_id,
            "blog_content": new_blog_data.blog_content,
            "timestamp": new_blog_data.timestamp,
            "likes": []
        }

        return {"new_blog": blog_dic}, 201
    except Exception as e:
        session.rollback()

        print(str(e))

        return abort(500, 'Internal server error')
    finally:
        session.close()


@blogs_bp.route('/delete/<string:blog_id>', methods=["DELETE"])
@validate_request_params(BlogIdParamsValidators)
@auth_required
def delete_blog(blog_id):
    try:
        print(blog_id)
        current_user = request.current_user

        user_data = get_user_by_email(current_user["email"], session)

        if not user_data:
            return "user not found", 404

        blog_to_delete = get_blog_by_id_and_user_id(blog_id, current_user["user_id"], session)

        if not user_data:
            return "blog not found", 404

        delete_current_blog(blog_to_delete, session)

        return "", 204
    except Exception as e:
        session.rollback()

        print(str(e))

        return abort(500, 'Internal server error')
    finally:
        session.close()
