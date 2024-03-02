from db import db
from datetime import datetime as dt
from sqlalchemy import Column, Integer, String, Boolean, Date


class Tarefa(db.Model):
    __tablename__ = 'tarefas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=False)
    data_inicio = Column(Date, nullable=False, default=dt.now().date())
    data_conclusao = Column(Date)
    concluida = Column(Boolean, nullable=False, default=False)
