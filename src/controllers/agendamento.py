from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

import datetime

from src import db
from src.models.tabelas import *
from src.packages import CriptografiaAES

agendamento_module = Blueprint('agendamento', __name__, url_prefix="/agendamento",
                    template_folder='../templates')



@agendamento_module.route("/create", methods=["GET"])
@login_required
def agendamento():
    if current_user.funcionario:
        encript = CriptografiaAES()

        servicos = Servicos.query.all()
        usuarios = Usuario.query.filter_by(funcionario=False).all()
        agendamentos = Agendamento.query.all()

        chaves_usuarios = list()
        for usuario in usuarios:
            chaves_usuarios.append(
                Tabela_chaves.query.filter_by(id_usuario = usuario.id_usuario).first()
            )

        chaves_usuarios_agendamentos = list()
        for agd in agendamentos:
            chaves_usuarios_agendamentos.append(
                Tabela_chaves.query.filter_by(id_usuario = agd.usuario_id).first()
            )

        return render_template('agendamento.html', servicos=servicos,
                               agendamentos=list(zip(agendamentos, chaves_usuarios_agendamentos)),
                               usuarios=list(zip(usuarios, chaves_usuarios)),
                               fn_descript=encript.descriptografar,
                               fn_data_hora=datetime.datetime.strftime)
    else:
        servicos = Servicos.query.all()
        return servicos, current_user #enviar para o front listar usuario pre checado


    
@agendamento_module.route("/create", methods=["POST"])
@login_required
def criar_agendamento():
    id_usuario = request.form.get('id_usuario')
    id_servico = request.form.get('id_servico')
    data_agendada = request.form.get('dataAgenda')
    hora_agendada = request.form.get('horarioAgenda')

    data_hora = None
    try:
        data_hora = datetime.datetime.strptime(f'{data_agendada} {hora_agendada}', '%Y-%m-%d %H:%M')
    except ValueError as e:
        data_hora = datetime.datetime.strptime(f'{data_agendada} {hora_agendada}', '%Y-%d-%m %H:%M')

    novo_agendamento = Agendamento(
        usuario_id = id_usuario,
        servico_id = id_servico,
        data_agendada = data_hora
    )
    db.session.add(novo_agendamento)
    db.session.commit()
    return 'pagina de agendamento'