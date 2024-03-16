from datetime import datetime as dt
from flask import Flask, render_template, redirect, request
from db import DATABASE_URI, db, migrate
from models import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI


# View Routes
@app.route("/", methods=["GET"])
def root():
    return redirect('/tarefas/listar')

@app.route("/login", methods=["GET"])
def login():
    return render_template('user/login.html')

@app.route("/registrar", methods=["GET"])
def register():
    return render_template('user/register.html')

@app.route("/tarefas/listar", methods=["GET"])
def index():
    tarefas = db.session.query(Tarefa).all()
    return render_template("tarefa/index.html", tarefas=tarefas)

@app.route('/tarefas/criar', methods=['GET'])
def create():
    return render_template("tarefa/create.html")

@app.route('/tarefas/<int:id>/edit', methods=['GET'])
def edit(id: int):
    tarefa = db.session.query(Tarefa).get(id)
    return render_template("tarefa/edit.html", tarefa=tarefa)

# Action Routes
@app.route("/tarefas/save", methods=["POST"])
def save():
    form_data = dict(request.form)
    
    tarefa = Tarefa(
        form_data.get("nome"),
        form_data.get("descricao"),
        dt.strptime(form_data.get("data_inicio"), "%Y-%m-%d").date(),
        form_data.get("data_conclusao")
    )
    db.session.add(tarefa)
    db.session.commit()
    
    return redirect("/tarefas/listar")

@app.route("/tarefas/update", methods=["POST"])
def update():
    form_data = dict(request.form)
    
    id = form_data.get('id')
    tarefa_db: Tarefa = db.session.query(Tarefa).get(id)
    
    tarefa_db.update(form_data)
    db.session.commit()
    
    return redirect("/tarefas/listar")


@app.route("/tarefas/<int:id>/delete", methods=["GET"])
def delete(id: int):
    tarefa = db.session.query(Tarefa).get(id)
    
    db.session.delete(tarefa)
    db.session.commit()

    return redirect("/tarefas/listar")

with app.app_context():
    db.init_app(app)
    migrate.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
