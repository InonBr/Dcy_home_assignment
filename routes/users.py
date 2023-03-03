from flask import Blueprint, request
from validators import SignupValidator
from utils import validate_request_body
from passlib.hash import sha256_crypt
from db.new_mysql_session import session
from models import User
import uuid


users_bp = Blueprint('api', __name__, url_prefix='/api')


@users_bp.route('/signup', methods=["POST"])
@validate_request_body(SignupValidator)
def signup():
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

    return new_user
