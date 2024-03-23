# /auth.py
from flask import flash, redirect
from flask_login import LoginManager
from db import db
from models import User

# Instância do LoginManager.
login_manager = LoginManager()


# Função que carrega o usuário logado no contexto de autenticação quando uma requisição é realizada.
@login_manager.user_loader
def load_user(id: int) -> User:
    return db.session.query(User).get(id)

# Função que lida quando uma requisição é feita em uma rota protegida quando o cliente não está autenticada.
@login_manager.unauthorized_handler
def unauthorized_handler():
    flash('Não autenticado. Por favor entre com sua conta.', category='error')
    return redirect('/login')