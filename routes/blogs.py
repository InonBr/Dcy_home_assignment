from flask import Blueprint, request, abort
from validators import NewBlogValidator
from utils import validate_request_body, auth_required
from db.new_mysql_session import session

blogs_bp = Blueprint('blogs_api', __name__, url_prefix='/api')


@blogs_bp.route('/new_blog', methods=["POST"])
@validate_request_body(NewBlogValidator)
@auth_required
def new_post():
    try:
        return "blog"
        # jwt_token = create_new_user(request.json, token, session)
        #
        # session.close()
        #
        # return {"user": jwt_token, "msg": "new user created successfully!"}, 201
    except Exception as e:
        session.rollback()
        session.close()

        print(str(e))

        if "Duplicate entry" in str(e):
            return {"error": "user already exist"}, 409

        return abort(500, 'Internal server error')
