from passlib.hash import sha256_crypt
from models import User
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
