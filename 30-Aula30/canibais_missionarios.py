
<<<<<<< HEAD
def Check_Adicionar(lista_geral):
    if len(barco) < 2:
        a == 0
        Perguntar_Selecao(lista_geral)
    else:
        continue

def Check_Retirar(lista_geral):
    if len(barco) > 0:
        a == 2
        Perguntar_Selecao(lista_geral, a)
    

def Check_Movimentar(lista_geral):
=======
canibais_partida = ['Canibal1', 'Canibal2', 'Canibal3']
missionarios_partida = ['Missionario1', 'Missionario2', 'Missionario3']
barco = []
canibais_chegada = []
missionarios_chegada = []

lista_geral = [canibais_partida, missionarios_partida, barco, canibais_chegada, missionarios_chegada]

def Check_Adicionar():
    if len(lista_geral[2]) < 2:
        

def Check_Retirar():
    pass

def Check_Movimentar():
>>>>>>> b028ec8e11df593ffa05d2dde9ef48a364d64dbd
    pass

def Embarcar():
    pass

def Desembarcar():
    pass

def Atravessar():
    pass

<<<<<<< HEAD
def Perguntar_Acao(lista_geral):
    while True:
        acao = input('''
(adicionar : Para adicionar um personagem ao barco
retirar: Para retirar um personagem do barco
movimentar: Para mover o barco ao outro lado do rio)
Digite o que deseja fazer: ''')
        if 'adicionar' in acao:
            Check_Adicionar(acao)
        if 'retirar' in acao:
            Check_Retirar(acao)
        if 'movimentar' in acao:
            Check_Movimentar(acao)
        else:
            print('\nVocê digitou um valor inválido')
            continue

def Perguntar_Selecao(lista_geral):
    a = 0
    while True:
        if a == 2:
            Selecao = input(f'Personagens disponíveis: {lista_geral[a]}')
            break
        elif:
            Selecao = input(f'Canibais disponíveis: {lista_geral[a+0]}\nMissionarios disponíveis: {lista_geral[a+1]}')
            break
        else:
            print('\nVocê digitou um valor inválido')
            continue

canibais_partida = ['canibal', 'canibal', 'canibal']
missionarios_partida = ['missionario', 'missionario', 'missionario']
barco = []
canibais_chegada = []
missionarios_chegada = []
lista_geral = [canibais_partida, missionarios_partida, barco, canibais_chegada, missionarios_chegada]

Perguntar_Acao(lista_geral)
=======
def Definir_Acao():
    while True:
        acao = input('''
        (adicionar : Para adicionar um personagem ao barco
        retirar: Para retirar um personagem do barco
        movimentar: Para mover o barco ao outro lado do rio)
        Digite o que deseja fazer: ''')

        if 'adicionar' in acao:
            Check_Adicionar()
            break
        elif 'retirar' in acao:
            Check_Retirar()
            break
        elif 'movimentar' in acao:
            Check_Movimentar()
            break
        else:
            print('\nVocê digitou uma ação inválida.')
            continue
    


Definir_Acao()
>>>>>>> b028ec8e11df593ffa05d2dde9ef48a364d64dbd
