from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv
import os
import jwt

load_dotenv()

token = os.getenv("TOKEN")


def validate_request_body(schema):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            body = schema()

            if not body.validate():
                return jsonify({"errors": body.errors}), 400
            return f(*args, **kwargs)

        return wrapper

    return decorator


def auth_required(f):
    @wraps(f)
    def decode(*args, **kwargs):
        token_test = request.headers.get("Authorization")
        try:
            if token_test is not None:
                current_user = jwt.decode(token_test, token, algorithms=["HS256"])
                request.current_user = current_user
            else:
                return jsonify({'msg': 'Token was not provided!'}), 403

        except jwt.exceptions.DecodeError:
            return jsonify({'msg': 'Token is invalid!'}), 403

        return f(*args, **kwargs)

    return decode
