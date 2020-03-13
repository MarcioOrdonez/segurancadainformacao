import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy



def create_app():
    app = Flask(__name__)
    project_dir = os.path.dirname(os.path.abspath(__file__))
    database_file = "sqlite:///banco de dados"
    app.config["SQLALCHEMY_DATABASE_URI"] = database_file
    db = SQLAlchemy(app)
    with app.app_context():
        from controllers.crud import module
        app.register_blueprint(module, url_prefix="/")

        db.create_all()
    return app


if __name__ == "__main__":
    create_app().run(port=3000)