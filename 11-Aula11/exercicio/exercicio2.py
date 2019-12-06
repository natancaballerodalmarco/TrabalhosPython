#--- 2- Crie um programa que calcule:
#   A rentabilidade anual de um investimento baseando-se em sua rentabilidade mensal(juros composto);
#   A rentabilidade deve ser apresentada em % e em R$;
#   Utilize métodos;

print('='*50, '\n')

from calculo_exercicio2 import calculo_montante

investimento = float(input('Quanto você investiu? '))
tempo = int(input('Por quantos meses você investiu? '))
juros = float(input('Qual foi a porcentagem do juros? '))

montante = calculo_montante(investimento, tempo, juros)
print(f'O montante foi {montante:.2f}')

print('\n', '='*50)