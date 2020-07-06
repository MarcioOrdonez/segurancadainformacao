from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from datetime import datetime

from src import db
from src.models.tabelas import *
from src.packages import CriptografiaAES
from src.utils.usuario_utils import user_is_funcionario

cripto = CriptografiaAES()

principal_module = Blueprint('principal', __name__, url_prefix="/",
                    template_folder='../templates')

@principal_module.route("", methods=["GET"])
def principal():
    if current_user.is_authenticated:
        chave_usuario = Tabela_chaves.query.filter_by(id_usuario=current_user.get_id()).first()
        is_funcionario = user_is_funcionario(chave_usuario, current_user)
        if is_funcionario:
            return redirect(url_for('agendamento.agendamento'))
        return redirect(url_for('usuario.perfil'))
    else:
        return redirect(url_for('auth.login'))