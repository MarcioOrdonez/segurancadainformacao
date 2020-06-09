from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from dotenv import load_dotenv
from pathlib import Path 

import os

db = SQLAlchemy()
migrate = Migrate()

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


def create_app():
    app = Flask(__name__)
    project_dir = os.path.dirname(os.path.abspath(__file__))
    # app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('MySQL_DB')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQL_DB')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from src.models import tabelas
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

@login_manager.user_loader
def load_user(user_id):
    from src.models import tabelas
    return Usuario.query.get(int(user_id))