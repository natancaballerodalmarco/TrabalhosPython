n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
operacao = int(input('''Qual operação matemática você deseja fazer?
(1 para soma)
(2 para subtração)
(3 para multiplicação)
(4 para divisão)
(5 para potenciação)
(6 para radiciação) '''))
if operacao==1:
    r1 = int(n1 + n2)
    print(f'O resultado da soma é: {r1}')

elif operacao==2:
    r2 = int(n1 - n2)
    print(f'O resultado da subtração é: {r2}')

elif operacao==3:
    r3 = int(n1 * n2)
    print(f'O resultado da mutiplicação é: {r3}')

elif operacao==4:
    r4 = float(n1 / n2)
    print(f'O resultado da divisão é: {r4:.3f}')

elif operacao==5:
    r5 = int(n1**n2)
    print(f'O resultado da potenciação é: {r5}')

elif operacao==6:
    r6 = float(n1**(1.0/n2))
    print(f'O resultado da radiciação é: {r6:.3f}')

else:
    print('Você digitou caracter inválido, tente novamente com uma das opções pedidas!')


if n1 < n2:
    print(f'{n1} é menor que {n2}!')

elif n1 > n2:
    print(f'{n1} é maior que {n2}!')

else:
    print(f'Os dois números são iguais!')
