from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

import datetime

from src import db
from src.models.tabelas import *

servicos_module = Blueprint('servicos', __name__, url_prefix="/servicos",
                    template_folder='../templates')

    

@servicos_module.route("/create", methods=["GET"])
@login_required
def servico():
    return 'tela de criar servicos'

@servicos_module.route("/create", methods=["POST"])
@login_required
def create_servico():
    nome = request.form.get('email')
    descricao = request.form.get('password')
    preco = request.form.get('preco')
    duracao = request.form.get('duracao')
    novo_servico = Servicos(nome = nome, descricao = descricao,
                    preco = preco, duracao = duracao)
    db.session.add(novo_servico)
    db.session.commit()
    return 'tela de criar servicos'

@servicos_module.route("/list", methods=["GET"])
@login_required
def list_servico():
    servicos = Servicos.query.all()
    return servicos