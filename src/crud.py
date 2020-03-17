from flask import Blueprint
from flask import request

from src import db

module = Blueprint('crud', __name__)


@module.route('/inserir', methods=["POST"])
def inserir():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    sexo = request.form.get('sexo')
    telefone = request.form.get('telefone')
    db.execute

@module.route("/get", methods=["GET"])
def get():
    return "asdasdasdasd"