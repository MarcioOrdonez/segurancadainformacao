from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    project_dir = os.path.dirname(os.path.abspath(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://root:admin@localhost/salao_cabeleireiro"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)

    with app.app_context():
        from src.controllers.crud import crud_bp

        app.register_blueprint(crud_bp)

        manager = Manager(app)

        return app