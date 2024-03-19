from datetime import datetime as dt
from flask import Blueprint, redirect, render_template, request
from flask_login import current_user, login_required
from db import db
from models import Tarefa, User


tarefa_bp = Blueprint('Tarefa', __name__)


# Views
@tarefa_bp.route("/", methods=["GET"])
def root():
    return redirect('/tarefas/listar')


@tarefa_bp.route("/tarefas/listar", methods=["GET"])
@login_required
def index():
    user: User = current_user
    tarefas = db.session.query(Tarefa)\
        .where(Tarefa.user_id == user.id).all()
    
    return render_template("tarefa/index.html", tarefas=tarefas, username=user.nome)


@tarefa_bp.route('/tarefas/criar', methods=['GET'])
@login_required
def create():
    user: User = current_user
    return render_template("tarefa/create.html", username=user.nome)


@tarefa_bp.route('/tarefas/<int:id>/edit', methods=['GET'])
@login_required
def edit(id: int):
    user: User = current_user
    tarefa = db.session.query(Tarefa).get(id)
    return render_template("tarefa/edit.html", tarefa=tarefa, username=user.nome)


# Action Routes
@tarefa_bp.route("/tarefas/save", methods=["POST"])
@login_required
def save():
    user: User = current_user
    form_data = dict(request.form)
    
    tarefa = Tarefa(
        form_data.get("nome"),
        form_data.get("descricao"),
        dt.strptime(form_data.get("data_inicio"), "%Y-%m-%d").date(),
        form_data.get("data_conclusao"),
        user.id
    )
    db.session.add(tarefa)
    db.session.commit()
    
    return redirect("/tarefas/listar")


@tarefa_bp.route("/tarefas/update", methods=["POST"])
@login_required
def update():
    form_data = dict(request.form)
    
    id = form_data.get('id')
    tarefa_db: Tarefa = db.session.query(Tarefa).get(id)
    
    tarefa_db.update(form_data)
    db.session.commit()
    
    return redirect("/tarefas/listar")


@tarefa_bp.route("/tarefas/<int:id>/delete", methods=["GET"])
@login_required
def delete(id: int):
    tarefa = db.session.query(Tarefa).get(id)
    
    db.session.delete(tarefa)
    db.session.commit()

    return redirect("/tarefas/listar")
