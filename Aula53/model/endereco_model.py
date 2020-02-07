import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

BaseAlchemy = declarative_base()

class EnderecoModel(BaseAlchemy):
    __tablename__ = 'Natan_Endereco'
    id = db.Column(db.Integer, primary_key=True)
    cidade = db.Column(db.String(length=45))
    bairro = db.Column(db.String(length=45))
    logradouro = db.Column(db.String(length=45))
    numero = db.Column(db.Integer)
    complemento = db.Column(db.String(length=45))

    def __str__(self):
        return f'id : {self.id} - cidade : {self.cidade} - bairro : {self.bairro} - logradouro : {self.logradouro} - numero : {self.numero} -  complemento : {self. complemento}'
