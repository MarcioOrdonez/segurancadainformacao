from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    project_dir = os.path.dirname(os.path.abspath(__file__))
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://root:admin@localhost/lgpd"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../salao.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    from src.models import tabelas
    db.init_app(app)
    db.create_all(app=app)
    migrate.init_app(app, db)

    with app.app_context():
        from src.controllers.crud import crud_bp

        app.register_blueprint(crud_bp)

        manager = Manager(app)
        manager.add_command('db', MigrateCommand)

        return app