#1 - Menu interativo com:
#---Cadastro da banda
#---Cadastro do álbum
#---Cadastro da música
#---Sair
menu = ''' 
                       CADASTRO FAIXAS

1 - Cadastrar artista
2 - Cadastrar álbum
3 - Cadastrar música
4 - Sair

Digite a opção desejada: '''

lista_artista = []
lista_album = []
lista_musica = []
while True:
    opcao = input(menu)
    if opcao == '1':
        lista_artista.append(input('Digite o nome do(a) artista: '))
    elif opcao == '2':
        lista_album.append(input('Digite o nome do álbum: '))
    elif opcao == '3':
        lista_musica.append(input('Digite o nome dda música: '))
    elif opcao == '4':
        print(f'''
        {lista_artista}
        {lista_album}
        {lista_musica}
        Volte sempre!''')
        break
    else:
        print('Caracter inválido')
