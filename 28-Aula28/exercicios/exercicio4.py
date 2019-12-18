# Aula 28 - 17-12-2019
# Listas

# DICA!!!!
# Procurem primeiro o padrão que estas listas vão apresentar! Depois de encontrado, faça o uso da linguagem
# para facilitar na hora de codar!


lista1 = [['frutas','verduras','legumes','preço'],
         ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
         ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha','cebolinha'],
         ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja'],
         [ [10.00, 2.56, 5.25, 9.5, 10.05, 15, 5.75], [2.99, 2.95, 3.5, 3.25, 5.89, 2.9, 2.5],
           [9.0, 5.0, 7.5, 1.75, 10.9, 5.99, 3.55] 
         ]
        ]


lista2 = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]

lista_vegetais = lista1[1:4]
lista_precos = lista1[4]
# print(lista_vegetais)
# print(lista_precos)
for a in range(3):
  list(zip(lista_vegetais, lista_precos))
  dicionario = dict(zip(lista_vegetais[a], lista_precos[a]))
print(dicionario)
# 1) Faça um dicionário com a lista1 onde cada elemento esteja junto com o seu respectivo
# preço. (Dica: Use a indexação e fatiamento para ajudar)
# print('='*150, '\n1-')
# dicionario = {}
# for i_slow in range(3):
#   for i_fast in range(7):
#     dicionario.append(lista_vegetais[i_slow][i_fast]:lista_precos[i_slow][i_fast])
# print(dicionario)

# 2) Com o dicionário, imprima os seguintes valores:
# 2.1) Preço do feijão
print('='*150, '\n2a-')

# 2.2) Preço da cebolinha
print('='*150, '\n2b-')

# 2.3) Preço da Alface lisa
print('='*150, '\n2c-')

# 2.4) Preço do Abacaxi
print('='*150, '\n2d-')

# 2.5) Preço do feijão branco.
print('='*150, '\n2e-')

# 3) Com a lista1 qual seria a média dos valores das frutas, verduras e legumes?
print('='*150, '\n3-')

# 4) Com a lista 1, Qual é o maior e menor valor das frutas, verduras e legumes?
print('='*150, '\n4-')

# 5) Adicione no cabeçalho da lista1 (entre o legumes e preço) a "roupa". Aṕos adicione de forma que fique 
# com a lista coerente 7 roupas e os seus preços.
print('='*150, '\n5-')

# 6) Salve esta lista em um arquivo .txt de moque que cada linha tenha o item e seu preço. 
print('='*150, '\n6-')

# 7) Com a lista2, crie uma lista com dicionário onde cada dicionário é um cadastro de uma pessoa.
print('='*150, '\n7-')

# 8) Organize a lista2, retirando o cabeçalho e junte os dados de modo que cada cliente ocupe uma lista. Após, salve os dados
# em um arquivo .txt 
print('='*150, '\n8-')

# 9) Criando uma fila. Uma fila é uma estrutura de dados onde o primeiro item que entra é o ultimo que sai. Resumindo, o item novo
# entra no indice 0 da lista e sai pelo ultimo indice. 
# Ex:
# >>> []
# >>> [1]
# >>> [2,1]
# >>> [3,2,1]
# >>> [3,2]
# >>> [3] 

# Crie um programa que adiciona novos clientes em uma fila e conforme vai atendendo, remova-os da fila do caixa da loja.
print('='*150, '\n9-')

# 10) Criando uma pilha. Uma pilha é uma estrutura de dados onde o primeiro que entra é o ultimo a sair. Resumindo,
# Os elementos são adicionados e removidos no mesmo lado da lista.
# Ex:
# >>> []
# >>> [1]
# >>> [1,2]
# >>> [1,2,3]
# >>> [1,2]
# >>> [1] 

# Crie um programa em que adicione os novos números na pilha. Após some eles removendo da pilha.
print('='*150, '\n10-')

print('='*150)