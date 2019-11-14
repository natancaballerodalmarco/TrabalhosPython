#  - Exercício 1 - Dcionário
#  - Escreva um programa que leia os dados de cerveja
#  - Cerveja : Marca, Tipo, IBU, ABV, EBC, Volume
#  - Crie um dicionário para armazenar os dados
#  - Imprima os dados do dicionário (não o dicionário completo)


marca = input('Indique a marca')
tipo = input('Indique o tipo: ')
ibu = int(input('Indique o IBU: '))
abv = float(input('Indique o ABV: '))
ebc = float(input('Indique o EBC: '))
volume = float(input('Indique o volume: '))

cerveja = {'Marca': marca, 'Tipo': tipo, 'IBU': ibu, 'ABV': abv, 'EBC': ebc, 'Volume': volume}
print(f"{cerveja['Marca']} | {cerveja['Tipo']} | {cerveja['IBU']} | {cerveja['ABV']} | {cerveja['EBC']} | {cerveja['Volume']}")
