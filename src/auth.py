from flask import flash, redirect
from flask_login import LoginManager
from db import db
from models import User


login_manager = LoginManager()


@login_manager.user_loader
def load_user(id: int) -> User:
    return db.session.query(User).get(id)


@login_manager.unauthorized_handler
def unauthorized_handler():
    flash('Não autenticado. Por favor entre com sua conta.', category='error')
    return redirect('/login')
