from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

import datetime

from src import db
from src.models.tabelas import *
from src.packages import CriptografiaAES
from src.utils.usuario_utils import user_is_funcionario

cripto = CriptografiaAES()

usuario_module = Blueprint('usuario', __name__, url_prefix="/usuario",
                           template_folder='../templates')


@usuario_module.route("/historico", methods=["GET","POST"])
@login_required
def get_historico():
    chave_usuario = Tabela_chaves.query.filter_by(id_usuario=current_user.get_id()).first()
    is_funcionario = user_is_funcionario(chave_usuario, current_user)

    historico = None

    if request.method == "GET":
        if is_funcionario:
            agendamentos = Agendamento.query.all()

            historico = list()
            for agendamento in agendamentos:
                chave_usuario = Tabela_chaves.query.filter_by(id_usuario=agendamento.usuario_id).first()
                historico.append((agendamento, chave_usuario))
        else:
            historico = {
                'agendamentos': Agendamento.query.filter_by(usuario_id=current_user.get_id()).all(),
                'chave_usuario': chave_usuario
            }

    elif request.method == "POST":
        if is_funcionario:
            usuario = Usuario.query.filter_by(usuario_id=request.form.get('id_usuario')).first()
            historico = Agendamento.query.filter_by(usuario=usuario).all()

    return render_template('historico.html', historico=historico, historico_is_list=type(historico) is list,
                           fn_decript=cripto.descriptografar, user_is_funcionario=is_funcionario)

# esses metodos nao irão mais existir, mas precisamos debater isso
# @usuario_module.route("/historico/delete_all", methods=["POST"])
# @login_required
# def delete_all_historico():
#     if not current_user.funcionario:
#         tabela_chaves = Tabela_chaves.query.filter_by(id_usuario = current_user.id_usuario)
#         # tabela_chaves = Tabela_chaves.query.filter_by(id_usuario = request.form.get("id_usuario")).first()
#         db.session.delete(tabela_chaves)
#         db.session.commit()


# @usuario_module.route("/historico/delete", methods=["POST"])
# @login_required
# def delete_one():
#     usuario_anonimo = Usuario.query.filter_by(id_usuario = 1).first() # pegar usuario anonimo
#     registro_id = request.form.get("registro_id")

#     registro = Agendamento.query.filter_by(id_agendamento = registro_id).first()
#     registro.usuario = usuario_anonimo # usuario_anonimo.id

#     db.session.commit()


@usuario_module.route("/delete", methods=["POST"])
@login_required
def delete_user():
    if current_user.funcionario:
        user_id = request.form.get('user_id')
        user = Usuario.query.filter_by(id_usuario = user_id).first()
    else:
        user = current_user

    historico = Agendamento.query.filter_by(usuario = user).all()

    usuario_anonimo = Usuario.query.filter_by(id_usuario = 1).first() # pegar usuario anonimo
    for registro in historico:
        registro.usuario = usuario_anonimo # id do usuario anônimo

    db.session.delete(user)
    db.session.commit()

    return 'deletado'

@usuario_module.route('/deleta_endereco', methods=['Post'])
@login_required
def deletar_end():
    endereco = Endereco.query.filter_by(id_usuario=current_user.id_usuario).first()
    db.session.delete(endereco)
    db.session.commit()
    return 'endereco deletado'

    return 'endereco não deletado'

@usuario_module.route('/alterar_endereco', methods=['Post'])
@login_required
def alterar_end():
    numero=int(request.form.get('numero'))
    cep=request.form.get('cep')
    comp=request.form.get('complemento')
    if numero > 0 and cep != "":
        endereco = Endereco.query.filter_by(id_usuario=current_user.id_usuario).first()
        endereco.cep=cep
        endereco.numero=numero
        endereco.complemento=comp
        db.session.commit()
        return "alterado endereco"
        
        
    return 'não alterado'
