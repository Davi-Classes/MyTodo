from flask import Blueprint, flash, redirect, render_template, request
from flask_login import login_required, login_user, logout_user
from db import db
from models import User



user_bp = Blueprint('User', __name__)


# View Routes
@user_bp.route("/login", methods=["GET"])
def index():
    return render_template('user/login.html')

@user_bp.route("/registrar", methods=["GET"])
def create():
    return render_template('user/register.html')


# Action Routes
@user_bp.route("/login", methods=['POST'])
def login():
    form_data = dict(request.form)

    nome = form_data.get('nome')
    senha = form_data.get('senha')
    lembrar = form_data.get('lembrar')

    user = db.session.query(User)\
        .where(User.nome == nome).first()
    
    if user is None or not user.verificar_senha(senha):
        flash('Credenciais Inválidas.', category='error')
        return redirect('/login')

    login_user(user, remember=lembrar)
    return redirect('/tarefas/listar')

@user_bp.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect('/login')

@user_bp.route("/registrar", methods=["POST"])
def save():
    form_data = dict(request.form)

    nome = form_data.get('nome')
    senha = form_data.get('senha')
    confirmar_senha = form_data.get('confirmar-senha')

    if senha != confirmar_senha:
        flash('As senhas não batem.', category='error')
        return redirect('/registrar')

    user_exists = db.session.query(User)\
        .where(User.nome == nome).first()

    if user_exists:
        flash('Usuário já existente', category='error')
        return redirect('/registrar')

    user = User(nome, senha)
    db.session.add(user)
    db.session.commit()

    flash('Usuário cadastrado com sucesso.', category='success')
    return redirect('/login')