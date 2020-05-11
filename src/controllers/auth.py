from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

import datetime

from src import db
from src.models.tabelas import *

auth_module = Blueprint('auth', __name__, url_prefix="/auth",
                    template_folder='../templates')


@auth_module.route("/login", methods=["GET"])
def login():
    return 'tela de login'


@auth_module.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = Usuario.query.filter_by(email=email).first()

    if not user and not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    return 'tela principal depois de logado'


@auth_module.route('/signup')
def signup():
    return 'tela de criação de usuario'

@auth_module.route('/signup', methods=['POST'])
def signup_post():
    user_email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    data_nascimento = request.form.get('data_nascimento')
    cpf = request.form.get('cpf')

    user = Usuario.query.filter_by(email=user_email).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    new_user = Usuario(nome=name, password=generate_password_hash(password,
                         method='sha256'),email=user_email, funcionario=False,
                         data_nascimento=datetime.datetime.now(), cpf=cpf)

    db.session.add(new_user)
    db.session.commit()

    return "vai pra tela de login"