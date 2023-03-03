from flask import Flask
from routes.users import users_bp
from db.new_mysql_session import mysql_connection_string
from db.database import sql_alchemy_db
from flask_migrate import Migrate
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = mysql_connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WTF_CSRF_ENABLED'] = False

sql_alchemy_db.init_app(app)
migrate = Migrate(app, sql_alchemy_db)

app.register_blueprint(users_bp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
