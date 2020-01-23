import sys
sys.path.append('C:/Users/900154/Desktop/Python/TrabalhosPython/37-Aula37')
from Controller.squad_controller import SquadController
from Model.squad import Squad

controller = SquadController()
lista = controller.listar_todos()