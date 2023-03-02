from flask import Flask
from routes.users import users_bp
from db import create_connection

app = Flask(__name__)

connection = create_connection()
print(connection)

app.register_blueprint(users_bp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
