import sys
sys.path.append('C:/Users/900154/Desktop/Python/TrabalhosPython/Squads')
from Inicio import SquadDao

class SquadController:
    dao = SquadDao
    def listar_todos(self):
        lsita_squads = []
        lista_tuplas = self.dao.listar_todos()
        for s in lista_tuplas:
            dicionario_squad = {'Id': 0, 'Nome' : '', 'Descricao': '', 'NumeroPessoas' : 0, 'LinguagemBackEnd': '', 'FrameworkFrontEnd': ''}
            dicionario_squad['Id'] = p[0]
            dicionario_squad['Nome'] = p[1]
            dicionario_squad['Descricao'] = p[2]
            dicionario_squad['NumeroPessoas'] = p[3]
            dicionario_squad['LinguagemBackEnd'] = p[4]
            dicionario_squad['FrameworkFrontEnd'] = p[5]
            lista_pessoas.append(dicionario_squad)
