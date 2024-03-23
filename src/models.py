from db import db
from datetime import datetime as dt, date
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class Tarefa(db.Model):
    __tablename__ = 'tarefas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=False)
    data_inicio = Column(Date, nullable=False, default=dt.now().date())
    data_conclusao = Column(Date)
    concluida = Column(Boolean, nullable=False, default=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="tarefas")

    def __init__(
        self, 
        nome: str, 
        descricao: str,
        data_inicio: date,
        data_conclusao: date,
        user_id: int
    ) -> None:
        self.nome = nome
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_conclusao = data_conclusao
        self.concluida =  True if data_conclusao is not None else False
        self.user_id = user_id

    def update(self, tarefa: dict):
        self.nome = tarefa.get('nome')
        self.descricao = tarefa.get('descricao')
        self.data_inicio = dt.strptime(tarefa.get('data_inicio'), '%Y-%m-%d')
        
        data_conclusao = tarefa.get('data_conclusao')
        if data_conclusao != '':
            self.data_conclusao = dt.strptime(data_conclusao, '%Y-%m-%d').date()
            self.concluida = True
        else:
            self.data_conclusao = None
            self.concluida = False


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    senha = Column(String(255), nullable=False)
    ativo = Column(Boolean, nullable=False, default=True)
		
    tarefas: Mapped[list["Tarefa"]] = relationship("Tarefa", back_populates="user")
		
    def __init__(self, nome: str, senha: str) -> None:
        self.nome = nome
        self.senha = generate_password_hash(senha)
    
    def verificar_senha(self, senha_plana: str) -> bool:
        return check_password_hash(self.senha, senha_plana)