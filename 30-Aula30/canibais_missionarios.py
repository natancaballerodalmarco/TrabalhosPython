def Embarcar():
    pass

def Desembarcar():
    pass

def Perguntar():
    pass

def Atravessar(saida, chegada, p1, p2 = None):
    pass

canibais_partida = ['Canibal1', 'Canibal2', 'Canibal3']
missionarios_partida = ['Missionario1', 'Missionario2', 'Missionario3']
barco = []
canibais_chegada = []
missionarios_chegada = []

while:
    acao = input('''
    (Adicionar : Para adicionar um personagem ao barco
    Retirar: Para retirar um personagem do barco
    Movimentar: Para mover o barco ao outro lado do rio)
    Digite o que deseja fazer: 
    ''')

    if acao.capitalize == 'Adicionar':
        selecionar = input(f'''
        Canibais Disponíveis:
        {canibais_partida}
        Missionários Disponíveis:
        {missionarios_partida}
        Digite o nome do personagem que você deseja adicionar ao barco: 
        ''')
        if 'Missionario' in selecionar.capitalize:
            barco.append()
    if acao.capitalize == 'Retirar':
        if len(barco) > 0:
