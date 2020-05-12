from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    # login_manager.init_app(app)
    project_dir = os.path.dirname(os.path.abspath(__file__))
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://root:admin@localhost/lgpd"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../salao.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    from src.models import tabelas
    db.init_app(app)
    db.create_all(app=app)
    migrate.init_app(app, db)

    with app.app_context():
        # from src.controllers import crud
        # app.register_blueprint(crud)

        from src.controllers import auth
        app.register_blueprint(auth)

        from src.controllers import agenda
        app.register_blueprint(agenda)

        from src.controllers import agendamento
        app.register_blueprint(agendamento)

        from src.controllers import servicos
        app.register_blueprint(servicos)

        manager = Manager(app)
        manager.add_command('db', MigrateCommand)

        return app