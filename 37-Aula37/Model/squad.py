from Model.backend import BackEnd
from Model.frontend import FrontEnd
from Model.sgbd import SGBD
class Squad:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao= ''
        self.numeropessoas = 0
        self.backend = BackEnd()
        self.frontend = FrontEnd()
        self.sgbd = SGBD()

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numeropessoas};{self.backend};{self.frontend};{self.sgbd}'

squad = Squad()
