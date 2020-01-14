
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
    pass

def Embarcar():
    pass

def Desembarcar():
    pass

def Atravessar():
    pass

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
