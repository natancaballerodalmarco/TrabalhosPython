import sys
sys.path.append(r'C:\Users\tan_u\OneDrive\Área de Trabalho\Python\TrabalhosPython\37-Aula37')
from Controller.squad_controller import SquadController
from Model.squad import Squad


squad = Squad()
squad.nome = 'legak'
squad.descricao = 'legal'
squad.numeropessoas = 3
squad.backend.nome = 'legal'
squad.frontend.nome = 'legal'
squad.sgbd.nome = 'legal'

controller = SquadController()
#id_salvo = controller.salvar(pessoa)
#pessoa_endereco = controller.buscar_por_id(id_salvo)
#print(pessoa_endereco)
print(controller.buscar_por_id(1))
