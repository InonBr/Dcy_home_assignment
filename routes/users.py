from flask import Blueprint

users_bp = Blueprint('main', __name__)


@users_bp.route('/')
def index():
    return 'Hello, World!'
