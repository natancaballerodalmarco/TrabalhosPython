
# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um metodo que leia 5 valores inteiros e retorne uma lista.
# Esta função deve ter tratamento de excessão evitando erro ValueError.

# 2 - Com a lista retornada, faça a multiplicação por 5 e salve o resultado
# em outra lista.

# Imprima a lista resultante

lista = []
lista_resultado = []
while len(lista) < 5:
    try:
        n = int(input('Digite um número inteiro: '))
        lista.append(n)
    except ValueError:
        print('Você digitou um caracter inválido!')


n = 0
for i in lista:
    n += i

lista_resultado.append(n*5)
print(lista_resultado)
