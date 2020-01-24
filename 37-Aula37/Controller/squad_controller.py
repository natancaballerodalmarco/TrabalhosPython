from Dao.squad_dao import SquadDao
from Model.squad import Squad
from Model.backend import BackEnd
from Model.frontend import FrontEnd
from Model.sgbd import SGBD
from Controller.backend_controller import BackEndController
from Controller.frontend_conotroller import FrontEndController
from Controller.sgdb_controller import SGDBController

class SquadController:
    dao = SquadDao()
    backend_controller = BackEndController()
    frontend_controller = FrontEndController()
    sgbd_controller = SGDBController()

    def listar_todos(self):
        lista_squads = []
        lista_tuplas = self.dao.listar_todos()
        for s in lista_tuplas:
            squad = Squad()
            squad.id =  s[0]
            squad.nome = s[1]
            squad.descricao = s[2]
            squad.numeropessoas = s[3]
            squad.backend = BackEnd()
            squad.backend.id = s[5]
            squad.backend.nome = s[6]
            squad.frontend = FrontEnd()
            squad.frontend.id = s[8]
            squad.forntend.nome = s[9]
            squad.sgdb = SGBD
            squad.sgdb.id = s[10]
            squad.sgdb.nome = s[11]
            lista_squads.append(squad)
        return lista_squads

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.id =  p[0]
        squad.nome = p[1]
        squad.sobrenome = p[2]
        squad.idade = p[3]
        squad.backend.id = p[5]
        squad.backend.logradouro = p[6]
        squad.backend.numero = p[7]
        squad.backend.complemento = p[8]
        squad.backend.bairro = p[9]
        squad.backend.cidade = p[10]
        squad.backend.cep = p[11]
        return squad

    def salvar(self, squad:Squad):
        squad.backend.id = self.backend_controller.salvar(squad.backend)
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        self.backend_controller.alterar(squad.backend)
        self.dao.alterar(squad)

    def deletar(self, id):
        self.dao.deletar(id)

