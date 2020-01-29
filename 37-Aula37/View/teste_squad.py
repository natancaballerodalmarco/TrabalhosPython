# Funcionando


import sys
sys.path.append(r'C:\Users\900154\Desktop\Python\TrabalhosPython\37-Aula37')
from Controller.squad_controller import SquadController
from Model.squad import Squad


squad = Squad()
squad.id = 2
squad.nome = 'teste03'
squad.descricao = 'testando3avez'
squad.numeropessoas = 3
squad.backend.id = 1
squad.backend.nome = 'testeBE03'
squad.frontend.id = 1
squad.frontend.nome = 'testeFE03'
squad.sgbd.id = 1
squad.sgbd.nome = 'testeSGBD03'

controller = SquadController()
# print(controller.buscar_por_id(3))
# lista_squads = controller.listar_todos()
# for i in range(len(lista_squads)):
#     print(lista_squads[i])
# controller.salvar(squad)
# controller.alterar(squad)
# controller.deletar(3)
