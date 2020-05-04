from flask import Blueprint, request, render_template, current_app as app
from sqlalchemy import create_engine

from src import db
from src.models.tabelas import *

crud_bp = Blueprint('crud', __name__, url_prefix="/",
                    template_folder='../templates')


@crud_bp.route("/inserir", methods=["GET", "POST"])
def inserir():
    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        sexo = request.form.get('sexo')
        telefone = request.form.get('telefone')

        engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])

        with engine.connect() as conn:
            result = conn.execute('SELECT * FROM funcionario')

            for data in result:
                print(data)

    return render_template('crud.html')

@crud_bp.route("/get", methods=["GET"])
def get():
    return "asdasdasdasd"