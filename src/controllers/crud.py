from flask import Blueprint, request, render_template, current_app as app
from sqlalchemy import create_engine
from datetime import date

from src import db
from src.models.tabelas import *

crud_bp = Blueprint('crud', __name__, url_prefix="/",
                    template_folder='../templates')


@crud_bp.route("/inserir", methods=["GET", "POST"])
def inserir():
    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        data_nascimento = date.today()
        cpf = request.form.get('cpf')
        password = request.form.get('password')
        novo_usuario = Usuario(nome = nome, email = email, data_nascimento = data_nascimento, cpf = cpf, password = password, funcionario=False)
        db.session.add(novo_usuario)
        db.session.commit()
        engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])

        # with engine.connect() as conn:
        #     result = conn.execute('SELECT * FROM usuarios')

        #     for data in result:
        #         print(data)
    return render_template('crud.html')

@crud_bp.route("/get", methods=["GET"])
def get():
    return "asdasdasdasd"