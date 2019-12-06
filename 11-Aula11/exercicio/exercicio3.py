#--- 3- Crie um programa para calculo de investimentos;
#   Solicitar o valor a ser investido no tesouro Selic;
#   (Considerar o valor do tesouro Selic hoje);
#   Calcular o valor total até o vencimento do título;
#   Utilize métodos;

print('='*50, '\n')

from calculo_exercicio3 import calculo_montante

cotas = float(input('Quantas cotas você deseja comprar?( > 0.01 ) '))
tempo = int(input('Irá vencer em quantos meses? '))
# juros = float(input('Qual foi a porcentagem do juros? '))

montante = calculo_montante(cotas, tempo)
print(f'O montante foi {montante:.2f}')

print('\n', '='*50)
