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

@app.route("/tarefas/listar", methods=["GET"])
def index():
    tarefas = db.session.query(Tarefa).all()
    return render_template("index.html", tarefas=tarefas)

@app.route('/tarefas/criar', methods=['GET'])
def create():
    return render_template("create.html")

# Action Routes
@app.route("/tarefas", methods=["POST"])
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


@app.route("/tarefas/<int:id>/delete", methods=["GET"])
def delete(id: int):
    pass
    # for i, tarefa in enumerate(tarefas):
    #     if tarefa.get("id") == id:
    #         tarefas.pop(i)
    #         return redirect("/tarefas/listar")

    # return render_template(
    #     "index.html", tarefas=tarefas, message="Tarefa não encontrada"
    # )

with app.app_context():
    db.init_app(app)
    migrate.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
