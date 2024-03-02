from datetime import datetime as dt
from flask import Flask, render_template, redirect, request
from db import db, migrate
from models import Tarefa


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/task_list'


# View Routes
@app.route("/tarefas/listar", methods=["GET"])
def index():
    pass
    # return render_template("index.html", tarefas=tarefas)

@app.route('/tarefas/criar', methods=['GET'])
def create():
    return render_template("create.html")

# Action Routes
@app.route("/tarefas", methods=["POST"])
def save():
    form_data = dict(request.form)

    # tarefa = {
    #     "id": get_new_id(tarefas),
    #     "nome": form_data.get("nome"),
    #     "descricao": form_data.get("descricao"),
    #     "data_inicio": dt.strptime(form_data.get("data_inicio"), "%Y-%m-%d").date(),
    #     "data_conclusao": None,
    #     "concluida": False,
    # }
    # tarefas.append(tarefa)

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
