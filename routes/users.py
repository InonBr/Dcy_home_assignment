from flask import Blueprint, request, abort
from validators import SignupValidator
from utils import validate_request_body
from dotenv import load_dotenv
from repositories import create_new_user
from db.new_mysql_session import session
import os

load_dotenv()

token = os.getenv("TOKEN")

users_bp = Blueprint('api', __name__, url_prefix='/api')


@users_bp.route('/signup', methods=["POST"])
@validate_request_body(SignupValidator)
def signup():
    try:
        jwt_token = create_new_user(request.json, token, session)

        session.close()

        return {"user": jwt_token, "msg": "new user created successfully!"}, 201
    except Exception as e:
        session.rollback()

        print(str(e))

        if "Duplicate entry" in str(e):
            return {"error": "user already exist"}, 409

        return abort(500, 'Internal server error')
