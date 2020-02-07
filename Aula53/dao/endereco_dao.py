from Aula53.dao.base_dao import BaseDao
from Aula53.model.endereco_model import EnderecoModel


class EnderecoDao(BaseDao):
    def list_all(self):
        return self.sessao.query(EnderecoModel).all()
