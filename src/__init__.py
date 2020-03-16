import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy



def create_app():
    app = Flask(__name__)
    project_dir = os.path.dirname(os.path.abspath(__file__))
    database_file = "sqlite:////salao_cabelereiro"
    app.config["SQLALCHEMY_DATABASE_URI"] = database_file
    db = SQLAlchemy(app)
    db.init_app(app)
    with app.app_context():
        from controllers import module
        app.register_blueprint(module, url_prefix="/")
    return app, db


if __name__ == "__main__":
    app,db = create_app()
    app.run(port=3000)