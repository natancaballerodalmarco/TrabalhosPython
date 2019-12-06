# 1 - O programa deve ter um menu interativo com cabeçalho , local para:
# # Cadastro de clientes
# # Ver clientes cadastrados
# # Cadastro de produtos
# # Ver produtos cadastrados
# # Venda de produtos
# # Relatório de vendas
# # Sair
# Deve repetir até a opção sair ser chamada


menu = '''
################################################################################
#                       I Fesival de Cerveja em Ituroró                        #
################################################################################

1 - Cadastro de clientes
2 - Ver clientes cadastrados
3 - Cadastro de produtos
4 - Ver produtos cadastrados
5 - Venda de produtos
6 - Relatório de vendas
7 - Sair

Digite a opção desejada: '''


# opcao = input(menu)
while True:
    opcao = input(menu)
    if opcao == '1':
        print('Cadastro de cliente')
    elif opcao == '2':
        print('Ver clientes cadastrados')
    elif opcao == '3':
        print('Cadastro de produtos')
    elif opcao == '4':
        print('Ver produtos cadastrados')
    elif opcao == '5':
        print('Vendas')
    elif opcao == '6':
        print('Relatório de vendas')
    elif opcao == '7':
        print('Sair')
        break
    else:
        print('Caracter imválido')
