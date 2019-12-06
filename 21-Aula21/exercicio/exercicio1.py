# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.

print('='*50, '\n')
controle = 'n'
while controle != 's':
    try:
        numero1 = int(input('Digite um número inteiro:' ))
        numero2 = int(input('Digite outro número inteiro: '))
    except ValueError:
        print('Você digitou um caracter inválido!!')
        continue
    try:
        resultado_soma = numero1 + numero2 
        print(f'O resultado da soma é: {resultado_soma}')

        resultado_subtacao = numero1 - numero2 
        print(f'O resultado da subtração é: {resultado_subtacao}')

        resultado_multiplicacao = numero1 * numero2 
        print(f'O resultado da multiplicação é: {resultado_multiplicacao}')

        resultado_divisao = numero1 / numero2 
        print(f'O resultado da divisão é: {resultado_divisao}')
        
    except ZeroDivisionError:
        print('Não é possível dividir por 0!!')

    controle = input('Se você quer parar, digite "s"')


#################### até aqui tudo bem! ##########################

# 3 - faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# 4 - Faça outro tratamento de exceção para evitar que divida um numero
# por zero.
