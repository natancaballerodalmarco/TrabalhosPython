#Learn more or give us feedback
# Aula 18 - 03-11-2019

# interação de lista com o for

# Usando o comando for vamos fazer uma interação de varialvel tipo coleção. A interação é (simplificadamente) 
# percorer toda a variavel e isolar seu valores.

# 1.1 Com a seguinte lista, use o for para interar esta tupla  e apresentar (usando o f-string) O nome da cerveja, 
# tipo da cerveja, o IBU da cerveja e o preço dela.

cerveja = (('marca', 'tipo', 'ibu','preço'),
           ('Skol','IPA','ultra-leve',3.50),
           ('Brahma','lager','leve/media',3.45),
           ('Kaiser','Americam Larger','leve',2.35),
           ('Sol','larger mão','agua',1.19)
          )


cabecalho = cerveja[0]
informacoes = cerveja[1:]
# print(informacoes)
# print(cabecalho)

for informacao in informacoes:
    for i in range(4):
        print(f'{cabecalho[0]} {informacao[0]}')

# 1.2 Crie uma função que receba esta tupla e devolva uma lista com um dicionários referenciando cada uma destas 
# cervejas.

def recebe(cerveja):
    cabe = cerveja[0]
    dados = cerveja[1:]
    lista_cerva = []
    for dados_cerveja in  dados:
        dicionario = {cabe[0]:dados_cerveja, cabe[1]:dados_cerveja[1],
                      cabe[2]:dados_cerveja[2], cabe[3]:dados_cerveja[3]}
        lista_cerva.append(dicionario)
    return

print(recebe(cerveja))
[
{'marca', 'tipo', 'ibu','preço'},
{'Skol','IPA','ultra-leve',3.50},
{'Brahma','lager','leve/media',3.45},
{'Kaiser','Americam Larger','leve',2.35},
{'Sol','larger mão','agua',1.19}
]
