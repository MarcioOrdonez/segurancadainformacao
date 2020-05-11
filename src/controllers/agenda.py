from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

import datetime

from src import db
from src.models.tabelas import *

agenda_module = Blueprint('agenda', __name__, url_prefix="/agenda",
                    template_folder='../templates')


@agendamento_module.route("/create", methods=["GET"])
@login_required
def agenda():
    if current_user.funcionario:
        agendamentos = Agendamento.query.all()
        return agendamentos  #enviar para o front listar
    else:
        agendamentos = Agendamento.query.filter_by(id_usuario = current_user.id)
        return agendamentos #enviar para o front listar usuario pre checado




