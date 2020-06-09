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


app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('MySQL_DB)
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

    from src.controllers import auth
    app.register_blueprint(auth)

    from src.controllers import agendamento
    app.register_blueprint(agendamento)

    from src.controllers import servicos
    app.register_blueprint(servicos)

    from src.controllers import usuario
    app.register_blueprint(usuario)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

@login_manager.user_loader
def load_user(user_id):
    from src.models import tabelas
    return tabelas.Usuario.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=os.getenv("PORT"))