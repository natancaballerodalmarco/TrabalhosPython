from Dao.squad_dao import SquadDao
from Model.squad import Squad
from Model.backend import BackEnd
from Controller.backend_controller import BackEndController

class SquadController:
    dao = SquadDao()
    backend_controller = BackEndController()

    def listar_todos(self):
        lista_squads = []
        lista_tuplas = self.dao.listar_todos()
        for p in lista_tuplas:
            squad = Squad()
            squad.id =  p[0]
            squad.nome = p[1]
            squad.sobrenome = p[2]
            squad.idade = p[3]
            squad.backend = BackEnd()
            squad.backend.id = p[5]
            squad.backend.logradouro = p[6]
            squad.backend.numero = p[7]
            squad.backend.complemento = p[8]
            squad.backend.bairro = p[9]
            squad.backend.cidade = p[10]
            squad.backend.cep = p[11]
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

