from flask import Blueprint, request, abort
from validators import SignupValidator
from utils import validate_request_body
from passlib.hash import sha256_crypt
from db.new_mysql_session import session
from models import User
from dotenv import load_dotenv
import os
import uuid
import jwt

load_dotenv()

token = os.getenv("TOKEN")

users_bp = Blueprint('api', __name__, url_prefix='/api')


@users_bp.route('/signup', methods=["POST"])
@validate_request_body(SignupValidator)
def signup():
    try:
        body = request.json
        new_user_id = uuid.uuid4().hex
        crypt_password = sha256_crypt.encrypt(body["password"])

        new_user = User(
            user_id=new_user_id,
            first_name=body['first_name'],
            last_name=body['last_name'],
            email=body['email'],
            password=crypt_password
        )

        session.add(new_user)
        session.commit()

        payload = {
            'user_id': new_user_id,
            "first_name": body['first_name'],
            "last_name": body['last_name'],
            'email': body["email"]
        }

        jwt_token = jwt.encode(payload, token, algorithm='HS256')

        return {"user": jwt_token, "msg": "new user created successfully!"}, 201

    except Exception as e:
        # Catch any exception and return a 500 error
        users_bp.logger.exception(str(e))

        abort(500, 'Internal server error')
