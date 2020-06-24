from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

import datetime

from src import db
from src.models.tabelas import *

servicos_module = Blueprint('servicos', __name__, url_prefix="/servicos",
                    template_folder='../templates')

    

@servicos_module.route("/create", methods=["GET","POST"])

def servico():
    if request.method == 'GET':
        return render_template('servico.html')
    if request.method == 'POST':
        nome = request.form.get('nomeServico')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        duracao = request.form.get('duracao')
        novo_servico = Servicos(nome = nome, descricao = descricao,
                        preco = preco, duracao = duracao,
                        disponibilidade = True)
        db.session.add(novo_servico)
        db.session.commit()
        return redirect(url_for('servicos.list_servico'))


@servicos_module.route("/list", methods=["GET"])
def list_servico():
    lista = Servicos.query.all()
    return render_template('list.html', lista=lista) 