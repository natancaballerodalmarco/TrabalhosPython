# Aula 21 - 16-12-2019
#Funções para listas

from geradorlista import lista_simples_int

from random import randint


lista1 = lista_simples_int(randint(5,100))
lista2 = lista_simples_int((randint(5,75)))
lista3 = lista_simples_int(randint(5,70))


# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:


# 1.1) Qual é o tamanho da lista1?
print('='*150)

tamanho = len(lista1)
print(f'1- O tamanho da lista é {tamanho}')

print('\n', '='*150)

# 1.2) Qual é o maior valor da lista2?
maximo = max(lista2)
print(f'2- O valor máximo é {maximo}')

print('\n', '='*150)

# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?
maior = int(max(lista2))
menor = int(min(lista2))
print(f'3- A soma entre {maior} e {menor} é {maior + menor}')

print('\n', '='*150)


# 1.4) Qual é a média aritmética da lista1?
soma = sum(lista1)
elementos = len(lista2)
print(f'4- A média dos elementos da lista 1 é {soma / elementos}')

print('\n', '='*150)

# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)
s_lista1 = int(sum(lista1))
s_lista2 = int(sum(lista2))
s_lista3 = int(sum(lista3))
s_total = s_lista1 + s_lista2 + s_lista3
print(f'''5- A soma da lista1 é {s_lista1}
A soma da lista2 é {s_lista2}
A soma da lista3 é {s_lista3}
A soma de todas as lista é {s_total}
''')

print('='*150)

# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.
for a in range(len(lista1)):
    print(f'O valor na posição {a} é {lista1[a]}')

print('\n', '='*150)

# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError
def item_lista1(indice):
    try:
        return lista1[indice]
    except:
        pass

def item_lista2(indice):
    try:
        return lista2[indice]
    except:
        pass

def item_lista3(indice):
    try:
        return lista3[indice]
    except:
        pass

lista_indices = [5, 9, 10, 25]

for i in lista_indices:
    try:
        print(f'O valor da posição {i} da lista 1 é: {item_lista1(i)}')
        # print(f'O valor da posição 9 da lista 1 é: {lista1[9]}')
        # print(f'O valor da posição 10 da lista 1 é: {lista1[10]}')
        # print(f'O valor da posição 25 da lista 1 é: {lista1[25]}')
        print(f'O valor da posição {i} da lista 2 é: {item_lista2(i)}')
        # print(f'O valor da posição 9 da lista 2 é: {lista2[9]}')
        # print(f'O valor da posição 10 da lista 2 é: {lista2[10]}')
        # print(f'O valor da posição 25 da lista 2 é: {lista2[25]}')
        print(f'O valor da posição {i} da lista 3 é: {item_lista3(i)}')
        # print(f'O valor da posição 9 da lista 3 é: {lista3[9]}')
        # print(f'O valor da posição 10 da lista 3 é: {lista3[10]}')
        # print(f'O valor da posição 25 da lista 3 é: {lista3[25]}')
    except IndexError:
        print('SEGUE A VIDA')

print('\n', '='*150)


# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).
tamanho_lista1 = len(lista1)
tamanho_lista2 = len(lista2)
tamanho_lista3 = len(lista3)
if tamanho_lista1 > tamanho_lista2 and tamanho_lista1 > tamanho_lista3:
    print('A lista 1 é a maior!')
elif tamanho_lista2 > tamanho_lista1 and tamanho_lista2 > tamanho_lista3:
    print('A lista 2 é a maior!')
elif tamanho_lista3 > tamanho_lista2 and tamanho_lista3 > tamanho_lista1:
    print('A lista 3 é maior')
else:
    print('Duas listas são do mesmo tamanho')

print('\n', '='*150)

# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.
max_lista1 = max(lista1)
max_lista2 = max(lista2)
max_lista3 = max(lista3)
min_lista1 = min(lista1)
min_lista2 = min(lista2)
min_lista3 = min(lista3)
if min_lista1 <= min_lista2 and min_lista1 <= min_lista3:
    minimo = min_lista1
elif min_lista2 <= min_lista1 and min_lista2 <= min_lista3:
    minimo = min_lista2
elif min_lista3 <= min_lista1 and min_lista3 <= min_lista2:
    minimo = min_lista3
print(f'O resultado da conta é {max_lista1 + max_lista2 + max_lista3 - minimo}')

print('\n', '='*150)

# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas

max_lista1 = max(lista1)
max_lista2 = max(lista2)
max_lista3 = max(lista3)
min_lista1 = min(lista1)
min_lista2 = min(lista2)
min_lista3 = min(lista3)

print(f'A soma entre os maiores e menores valores é {max_lista1 + max_lista2 + max_lista3 + min_lista1 + min_lista2 + min_lista3}')

print('\n', '='*150)
