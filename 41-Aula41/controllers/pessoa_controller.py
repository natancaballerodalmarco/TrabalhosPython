from flask import Flask
from flask_restful import Resource

from daos.pessoa_dao import PessoaDao

class  PessoaController(Resource):
    def __init__(self):
        self.dao = PessoaDao

    def get(self):
        return self.dao.listar_todos

    def put(self):
        return self.dao.cadastrar

    def post(self):
        return self.dao.alterar

    def delete(self):
        return self.dao.deletar
