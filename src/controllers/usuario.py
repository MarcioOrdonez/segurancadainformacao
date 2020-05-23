from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

import datetime

from src import db
from src.models.tabelas import *

usuario_module = Blueprint('usuario', __name__, url_prefix="/usuario",
                    template_folder='../templates')

@usuario_module.route("/historico", methods=["GET"])
@login_required
def get_historico():
    if request.method == "GET":
        if current_user.funcionario:
            histotico = Agendamento.query.all()
        else:
            histotico = Agendamento.funcario.filter_by(id_usuario = current_user.id)
    elif request.method == "POST":
        if current_user.funcionario:
            historico = Agendamento.query.filter_by(id_usuario = request.form.get('id_usuario'))
    return histotico # retorna a lista de historico referente o usuario logado

@usuario_module.route("/historico/delete_all", methods=["POST"])
@login_required
def delete_all_historico():
    if not current_user.funcionario:
        historico = Agendamento.query.filter_by(id_usuario = current_user.id)
        for registro in historico:
            registro.id_user = 1 #usuario_anonimo.id
        db.session.commit()


@usuario_module.route("/historico/delete", methods=["POST"])
@login_required
def delete_one():
    registro_id = request.form.get("registro_id")
    registro = Agendamento.query.filter_by(id = registro_id)
    registro.id_usuario = 1 # usuario_anonimo.id

@usuario_module.route("/delete", methods=["POST"])
@login_required
def delete_user():
    if current_user.funcionario:
        user_id = request.form.get('user_id')
        user = User.query.filter_by(id = user_id)
    else:
        user_id = current_user.id
        user = User.query.filter_by(id = user_id)
    historico = Agendamento.query.filter_by(id_user = user_id)
    for registro in historico:
        registro.id_user() = 1 #id do usuario anonimo
    db.session.delete(user)
    db.session.commit()
    return 'deletado'
    