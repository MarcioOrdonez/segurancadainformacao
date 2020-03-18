import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    project_dir = os.path.dirname(os.path.abspath(__file__))
    database_file = "sqlite:////salao_cabelereiro"
    app.config["SQLALCHEMY_DATABASE_URI"] = database_file
    db.init_app(app)
    with app.app_context():
        from src.crud import module
        app.register_blueprint(module, url_prefix="/")
    return app


if __name__ == "__main__":
    app,db = create_app()
    app.run(port=3000)