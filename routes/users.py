from flask import Blueprint, jsonify
from validators import SignupValidator

users_bp = Blueprint('api', __name__, url_prefix='/api')


@users_bp.route('/signup', methods=["POST"])
def index():
    body = SignupValidator()

    if not body.validate():
        print(dict(body.errors))
        return jsonify({"errors": dict(body.errors)}), 400

    # first_name = form.first_name.data
    # last_name = form.last_name.data
    # email = form.email.data
    # password = form.password.data

    return 'Hello, World!'
