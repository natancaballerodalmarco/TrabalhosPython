print('='*50, '\n')
nome = input('Qual o seu nome?')
idade = int(input('Qual a sua idade?'))
A = False
if idade > 17:
    A = True
#    print(f'Olá {nome}, você já pode utilizar o mercado tech para comprar bebidas alcoólicas!')
#else:
#    print(f'Olá {nome}, você ainda não pode comprar bebidas alcoólicas no mercado tech!')

produto = input('Qual o produto? ')
categoria = (input('O produto é alcoólico? '))
B = False
print(f'Olá {nome}')
if categoria == 'sim':
    B = True
if B == False:
    print(f'Você pode comprar {produto}')
elif A and B == True:
    print(f'Você pode comprar {produto}')
else:
    print(f'Você não pode comprar {produto}')
    