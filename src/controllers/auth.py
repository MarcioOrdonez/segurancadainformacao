from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

import datetime

from src import db
from src.models.tabelas import *
from src.packages import CriptografiaAES

auth_module = Blueprint('auth', __name__, url_prefix="/auth",
                    template_folder='../templates')


@auth_module.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        cripto= CriptografiaAES()
        email = request.form.get('email')
        password = request.form.get('senha')

        user = Usuario.query.filter_by(email=email).first()

        if not user:
            flash('Por favor cheque suas informações e tente novamente! ')
            return redirect(url_for('auth.login'))
        else:
            chave = Tabela_chaves.query.filter_by(id_usuario=user.id_usuario).first()
            password = cripto.criptografar(chave.chave_privada, password)
            if password == user.password:
                pass
            login_user(user)

        return 'tela principal depois de logado'


@auth_module.route('/registrar', methods=["GET","POST"])
def registrar():
    if request.method == 'GET':
        return render_template('registrar.html')
    if request.method == 'POST':
        cripto= CriptografiaAES()
        chave = cripto.criaChave()

        user_email = request.form.get('email')
        name = cripto.criptografar(chave["chave"],request.form.get('nome'))
        password = request.form.get('senha')
        data_nascimento = None

        try:
            data_nascimento = datetime.datetime.strptime(request.form.get('data'),'%Y-%m-%d').date()
        except ValueError as e:
            data_nascimento = datetime.datetime.strptime(request.form.get('data'),'%Y-%d-%m').date()

        data_nascimento = cripto.criptografar(chave["chave"],data_nascimento)
        # data_nascimento = cripto.criptografar(chave_publica,datetime.datetime.now())
        cpf = cripto.criptografar(chave["chave"],request.form.get('cpf'))

        user = Usuario.query.filter_by(email=user_email).first()

        if user:
            flash('Email de usuario ja existe!')
            return redirect(url_for('auth.signup'))

        new_user = Usuario(nome=name, password=cripto.criptografar(chave["chave"],password),
                            email=user_email, funcionario=True,
                            data_nascimento=data_nascimento, cpf=cpf)

        db.session.add(new_user)
        usuario = Usuario.query.filter_by(email=user_email).first()
        tabela_chaves = Tabela_chaves(id_usuario = usuario.id_usuario, chave_privada = chave["chave"])
        db.session.add(tabela_chaves)
        db.session.commit()

    return redirect(url_for('auth.login'))


@auth_module.route('/logout')
@login_required
def logout():
    logout_user()
    return 'tela inicial'