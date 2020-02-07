from flask import Flask
from flask_restful import Api

from controllers.pessoa_controller import PessoaController
from Aula41.controllers.endereco_controller import EnderecoController

app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/pessoa', endpoint='pessoas')
api.add_resource(PessoaController, '/api/pessoa/<int:id>', endpoint='pessoa')

api.add_resource(EnderecoController, '/api/endereco', endpoint='enderecos')
api.add_resource(EnderecoController, '/api/endereco/<int:id>', endpoint='endereco')


@app.route('/')
def inicio():
    return 'Bien Venuti'

app.run(debug=True, port=80)
