from Dao.squad_dao import SquadDao
from Model.squad import Squad
from Model.backend import BackEnd
from Model.frontend import FrontEnd
from Model.sgbd import SGBD
from Controller.backend_controller import BackEndController
from Controller.frontend_conotroller import FrontEndController
from Controller.sgbd_controller import SGBDController

class SquadController:
    dao = SquadDao()
    backend_controller = BackEndController()
    frontend_controller = FrontEndController()
    sgbd_controller = SGBDController()

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
            squad.sgbd = SGBD()
            squad.sgbd.id = s[10]
            squad.sgbd.nome = s[11]
            lista_squads.append(squad)
        return lista_squads

    def buscar_por_id(self, id):
        s = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.id =  s[1]
        squad.nome = s[1]
        squad.descricao = s[2]
        squad.numeropessoas = s[3]
        squad.backend = BackEnd()
        squad.backend.id = s[5]
        squad.backend.nome = s[6]
        squad.frontend = FrontEnd()
        squad.frontend.id = s[8]
        squad.forntend.nome = s[9]
        squad.sgbd = SGBD()
        squad.sgbd.id = s[10]
        squad.sgbd.nome = s[11]
        return squad

    def salvar(self, squad:Squad):
        squad.backend.id = self.backend_controller.salvar(squad.backend)
        squad.frontend.id = self.frontend_controller.salvar(squad.frontend)
        squad.sgbd.id = self.sgbd_controller.salvar(squad.sgbd)
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        self.backend_controller.alterar(squad.backend)
        self.frontend_controller.alterar(squad.frontend)
        self.sgbd_controller.alterar(squad.sgbd)
        self.dao.alterar(squad)

    def deletar(self, id):
        self.dao.deletar(id)

