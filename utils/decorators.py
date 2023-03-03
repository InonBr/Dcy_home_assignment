from functools import wraps
from flask import request, jsonify, abort


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
