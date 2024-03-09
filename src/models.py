from db import db
from datetime import datetime as dt, date
from sqlalchemy import Column, Integer, String, Boolean, Date


class Tarefa(db.Model):
    __tablename__ = 'tarefas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=False)
    data_inicio = Column(Date, nullable=False, default=dt.now().date())
    data_conclusao = Column(Date)
    concluida = Column(Boolean, nullable=False, default=False)

    def __init__(
        self, 
        nome: str, 
        descricao: str,
        data_inicio: date,
        data_conclusao: date
    ) -> None:
        self.nome = nome
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_conclusao = data_conclusao
        self.concluida =  True if data_conclusao is not None else False
