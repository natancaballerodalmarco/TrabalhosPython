import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

BaseAlchemy = declarative_base()

class PessoaModel(BaseAlchemy):
    __tablename__ = "Natan_Pessoa"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=45))
    sobrenome = db.Column(db.String(length=45))
    idade = db.Column(db.Integer)

    def __str__(self):
        return f'id : {self.id} - nome : {self.nome} - sobrenome : {self.sobrenome} - idade : {self.idade}'
