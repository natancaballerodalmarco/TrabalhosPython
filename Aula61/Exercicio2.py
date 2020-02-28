numero_binario = bin(int(input('Digite um número: ')))
string_binaria = str(numero_binario)
string_binaria = string_binaria[2:]

string_binaria = string_binaria.strip('0')
lista_zeros = string_binaria.split('1')

lista_lacunas_binarias = []
for lacuna_binaria in lista_zeros:
    tamanho_lacuna_binaria = len(lacuna_binaria)
    lista_lacunas_binarias.append(tamanho_lacuna_binaria)

maior_lacuna_binaria = max(lista_lacunas_binarias)
if maior_lacuna_binaria > 0:
    print(f'A maior lacuna binária do número é {maior_lacuna_binaria} ')
else:
    print('None')
