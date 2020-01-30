from flask import Flask
from flask_restful import Resource

class  PessoaController(Resource):
    def get(self):
        return "Controlador GET ALOHA"
    def put(self):
        return "Controlador PUT UAU"
    def post(self):
        return "Controlador POST YEAH"
    def delete(self):
        return "Controlador DELETE YEAH"
