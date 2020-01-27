import sys
sys.path.append('C:/Users/900154/Desktop/Python/TrabalhosPython/34-Aula34/Aula34-Endereco')
from controller.endereco_controller import EnderecoController

ec = EnderecoController()

for e in ec.listar_todos():
    print(e)
    
