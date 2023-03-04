from flask import Blueprint, request, abort
from validators import SignupValidator, LogInValidator
from utils import validate_request_body
from dotenv import load_dotenv
from repositories import create_new_user, get_user_by_email, verify_password_and_create_token
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
        session.close()

        print(str(e))

        if "Duplicate entry" in str(e):
            return {"error": "user already exist"}, 409

        return abort(500, 'Internal server error')


@users_bp.route('/login', methods=["POST"])
@validate_request_body(LogInValidator)
def login():
    try:
        email = request.json["email"]
        password = request.json["password"]

        user_data = get_user_by_email(email, session)

        if not user_data:
            return "user not found", 404

        jwt_token = verify_password_and_create_token(user_data, password, token)

        if not jwt_token:
            return "user not found", 404

        return {"user": jwt_token, "msg": "user login successfully!"}, 201
    except Exception as e:
        session.rollback()
        session.close()

        print(str(e))

        return abort(500, 'Internal server error')
