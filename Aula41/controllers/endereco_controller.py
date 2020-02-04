from flask_restful import Resource
from flask import request

from Aula41.models.endereco_model import EnderecoModel
from Aula41.daos.endereco_dao import EnderecoDao

class EnderecoController(Resource):
    def __init__(self):
        self.dao = EnderecoDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()

    def post(self):
        cidade = request.json['cidade']
        bairro = request.json['bairro']
        logradouro = request.json['logradouro']
        numero = int(request.json['numero'])
        complemento = request.json['complemento']
        endereco = EnderecoModel(cidade, bairro, logradouro, numero, complemento)
        return self.dao.insert(endereco)

    def put(self, id):
        cidade = request.json['cidade']
        bairro = request.json['bairro']
        logradouro = request.json['logradouro']
        numero = int(request.json['numero'])
        complemento = request.json['complemento']
        endereco = EnderecoModel(cidade, bairro, logradouro, numero, complemento, id)
        return self.dao.update(endereco)

    def delete(self, id):
        return self.dao.delete(id)
