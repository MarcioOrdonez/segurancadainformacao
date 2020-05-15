from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

import datetime

from src import db
from src.models.tabelas import *

servicos_module = Blueprint('servicos', __name__, url_prefix="/servicos",
                    template_folder='../templates')

    

@servicos_module.route("/create", methods=["GET"])
@login_required
def servico():
    return render_template('servico.html')
    # return 'asdasdasdasas'

@servicos_module.route("/create", methods=["POST"])
def create_servico():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    preco = request.form.get('preco')
    duracao = request.form.get('duracao')
    novo_servico = Servicos(nome = nome, descricao = descricao,
                    preco = preco, duracao = duracao)
    db.session.add(novo_servico)
    db.session.commit()
    return 'tela de criar servicos'

@servicos_module.route("/list", methods=["GET"])
def list_servico():
    servicos = Servicos.query.all()
    return servicos