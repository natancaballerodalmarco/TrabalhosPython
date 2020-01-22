import sys
sys.path.append('C:/Users/900154/Desktop/Python/TrabalhosPython/37-Aula37')
from Controller.squad_controller import SquadController
from Model.squad import Squad

squad = Squad()
squad.nome = 'HeadAche'
squad.descricao = 'So dor de Cabeca'
squad.numeropessoas = 8
squad.linguagembackend = 'JavaScript'
squad.frameworkfrontend = 'JavaScript'

controller = SquadController()
print(controller.listar_todos)