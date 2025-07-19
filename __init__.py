from flask import Flask
from app.routes import main
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    mysql.init_app(app)
    app.register_blueprint(main)
    return app