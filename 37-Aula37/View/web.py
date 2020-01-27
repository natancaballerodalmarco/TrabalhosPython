from flask import Flask, render_template, request, redirect
import sys
sys.path.append(r'C:\Users\900154\Desktop\Python\TrabalhosPython\37-Aula37')
from Controller.squad_controller import SquadController
from Controller.backend_controller import BackEndController
from Controller.frontend_conotroller import FrontEndController
from Controller.sgbd_controller import SGBDController
from Model.squad import Squad
from Model.backend import BackEnd
from Model.frontend import FrontEnd
from Model.sgbd import SGBD

app = Flask(__name__)
squad_controller = SquadController()
backend_controller = BackEndController()
frontend_controller = FrontEndController()
sgbd_controller = SGBDController()
nome = 'Cadastros'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    squads = squad_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista = squads)

@app.route('/cadastrar')
def cadastrar():
    squad = Squad()
    squad.backend = BackEnd()
    squad.frontend = FrontEnd()
    squad.sgbd = SGBD()
    if 'id' in request.args:
        id = request.args['id']
        squad = squad_controller.buscar_por_id(id)
    return render_template('cadastrar.html', titulo_app = nome, squad = squad )


@app.route('/excluir')
def excluir():
    id = int(request.args['id'])
    id_backend = request.args['id_backend']
    id_frontend = request.args['id_frontend']
    id_sgbd = request.args['id_sgbd']
    squad_controller.deletar(id)
    if id_backend != 'None':
        backend_controller.deletar(id_backend)
    if id_frontend != 'None':
        frontend_controller.deletar(id_frontend)
    if id_frontend != 'None':
        frontend_controller.deletar(id_frontend)
    return redirect('/listar')

@app.route('/salvar')
def salvar():
    squad = Squad()
    squad.id = request.args['id']
    squad.nome = request.args['nome']
    squad.descricao = request.args['descricao']
    squad.numeropessoas = request.args['numeropessoas']

    backend = BackEnd()
    backend.id = request.args['backend_id']
    backend.nome = request.args['nome']
    squad.backend = backend

    frontend = FrontEnd()
    frontend.id = request.args['frontend_id']
    frontend.nome = request.args['nome']
    squad.frontend = frontend

    sgbd = SGBD()
    sgbd.id = request.args['sgbd_id']
    sgbd.nome = request.args['nome']
    squad.sgbd = sgbd
    
    if pessoa.id == 0:
        pessoa_controller.salvar(pessoa)
    else:
        pessoa_controller.alterar(pessoa)
    return redirect('/listar')

app.run(debug=True)
