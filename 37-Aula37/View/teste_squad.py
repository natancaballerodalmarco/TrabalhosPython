import sys
sys.path.append(r'C:\Users\900154\Desktop\Python\TrabalhosPython\37-Aula37')
from Controller.squad_controller import SquadController
from Model.squad import Squad


squad = Squad()
squad.id = 3
squad.nome = 'teste03'
squad.descricao = 'testando 3a vez'
squad.numeropessoas = 3
squad.backend.id = 4
squad.backend.nome = 'testeBE03'
squad.frontend.id = 3
squad.frontend.nome = 'testeFE03'
squad.sgbd.id = 3
squad.sgbd.nome = 'testeSGBD03'

controller = SquadController()
# #id_salvo = controller.salvar(pessoa)
# #pessoa_endereco = controller.buscar_por_id(id_salvo)
# #print(pessoa_endereco)
# print(controller.buscar_por_id(3))
# lista_squads = controller.listar_todos()
# for i in range(len(lista_squads)):
#     print(lista_squads[i])
# controller.alterar(squad)
# controller.deletar(3)
