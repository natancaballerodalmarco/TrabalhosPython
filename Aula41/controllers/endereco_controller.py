from flask_restful import Resource
from flask import request

from Aula41.models.endereco_model import EnderecoModel
#from Aula41.daos.

class EnderecoController(Resource):
    def get(self):
        return 'Listando Endereco'

    def post(self):
        return 'Cadastrando Endereco'

    def put(self):
        return 'Alterando Endereco'

    def delete(self):
        return  'Deletando Endereco'
