from flask import Flask
from flask_restful import Api

from Controllers.pessoa_controller import PessoaController

app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/pessoapoxa')

@app.route('/')
def inicio():
    return 'Bien Venuti'

app.run(debug=True, port=80)
