from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

import datetime

from src import db
from src.models.tabelas import *
from src.packages import Criptografia

auth_module = Blueprint('auth', __name__, url_prefix="/auth",
                    template_folder='../templates')


@auth_module.route("/login", methods=["GET"])
def login():
    return render_template('login.html')


@auth_module.route('/login', methods=['POST'])
def login_post():
    cripto= Criptografia()
    email = request.form.get('email')
    password = request.form.get('password')

    user = Usuario.query.filter_by(email=email).first()

    if not user:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    else:
        password = cripto.criptografar(user.chave_publica, password)
        if password == user.password:
            return 'logado'

    return 'tela principal depois de logado'


@auth_module.route('/signup')
def signup():
    return render_template('usuario.html')

@auth_module.route('/signup', methods=['POST'])
def signup_post():
    cripto= Criptografia()
    chaves=cripto.criaChaves()
    chave_publica = chaves["public"]
    chave_privada = chaves["private"]

    user_email = request.form.get('email')
    name = cripto.criptografar(chave_publica,request.form.get('name'))
    password = request.form.get('password')
    # data_nascimento = request.form.get('data_nascimento')
    data_nascimento = cripto.criptografar(chave_publica,datetime.datetime.now())
    cpf = cripto.criptografar(chave_publica,request.form.get('cpf'))

    user = Usuario.query.filter_by(email=user_email).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    new_user = Usuario(nome=name, password=cripto.criptografar(chave_publica,password),
                        email=user_email, funcionario=True,
                        data_nascimento=data_nascimento, cpf=cpf, chave_publica=chave_publica )

    db.session.add(new_user)
    usuario = Usuario.query.filter_by(email=user_email).first()
    tabela_chaves = Tabela_chaves(id_usuario = usuario.id_usuario, chave_privada = chave_privada)
    db.session.add(tabela_chaves)
    db.session.commit()

    return "vai pra tela de login"