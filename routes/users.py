from flask import Blueprint, request
from validators import SignupValidator
from utils import validate_request_body

users_bp = Blueprint('api', __name__, url_prefix='/api')


@users_bp.route('/signup', methods=["POST"])
@validate_request_body(SignupValidator)
def signup():
    body = request.json

    print(body)

    return 'Hello, World!'
