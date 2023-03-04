from passlib.hash import sha256_crypt
from models import User
from sqlalchemy import text
import uuid
import jwt


def create_new_user(body, token, session):
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

    return jwt.encode(payload, token, algorithm='HS256')


def get_user_by_email(email, session):
    return session.query(User).filter(text("email = :email")).params(email=email).first()


def verify_password_and_create_token(user_data, password, token):
    verify = sha256_crypt.verify(password, user_data.password)

    if not verify:
        return verify

    payload = {
        'user_id': user_data.user_id,
        "first_name": user_data.first_name,
        "last_name": user_data.last_name,
        'email': user_data.email
    }

    return jwt.encode(payload, token, algorithm='HS256')

