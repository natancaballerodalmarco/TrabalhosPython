
from Dao.sgbd_dao import SGBDDao
from Model.sgbd import SGBD

class SGBDController:
    dao = SGBDDao()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, sgbd:SGBD):
        return self.dao.salvar(sgbd)

    def alterar(self, sgbd:SGBD):
        self.dao.alterar(sgbd)

    def deletar(self, id):
        self.dao.deletar(id)
