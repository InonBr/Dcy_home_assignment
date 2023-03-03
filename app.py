from flask import Flask
from routes.users import users_bp
from db.connect_db import host, db_user, db_name, password
from db.database import sql_alchemy_db
from flask_migrate import Migrate
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{password}@{host}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WTF_CSRF_ENABLED'] = False

sql_alchemy_db.init_app(app)
migrate = Migrate(app, sql_alchemy_db)

app.register_blueprint(users_bp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
