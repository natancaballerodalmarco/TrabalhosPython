#--- 1- Crie um programa que calcule:
#   O imposto ISS de um serviço de desevolvimento de software;
#   Utilize métodos;

from calculo_exercicio1 import calculo_iss

print('='*50, '\n')

custo = float(input('Digite o custo do serviço: '))
iss = calculo_iss(custo)

print(f'O imposto é {iss}')

print('\n', '='*50)