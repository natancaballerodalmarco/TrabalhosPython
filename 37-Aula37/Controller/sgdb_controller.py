
from Dao.sgdb_dao import SGDBDao
from Model.SGDB import SGDB

class SGDBController:
    dao = SGDBDao()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, sgdb:SGDB):
        return self.dao.salvar(sgdb)

    def alterar(self, sgdb:SGDB):
        self.dao.alterar(sgdb)

    def deletar(self, id):
        self.dao.deletar(id)
