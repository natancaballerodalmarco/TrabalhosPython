# Você recebe N contadores, inicialmente definidos como 0, e você tem duas operações possíveis:
#
# aumento (X) - o contador X é aumentado em 1,
# contador máximo - todos os contadores são definidos para o valor máximo de qualquer contador.
# Uma matriz não vazia A de M inteiros é fornecida. Essa matriz representa operações consecutivas:
#
# se A [K] = X, tal que 1 ≤ X ≤ N, a operação K é um aumento (X),
# se A [K] = N + 1, a operação K é o contador máximo.
# Por exemplo, dado o número N = 5 e a matriz A, de modo que:
#
#     A [0] = 3
#     A [1] = 4
#     A [2] = 4
#     A [3] = 6
#     A [4] = 1
#     A [5] = 4
#     A [6] = 4
# os valores dos contadores após cada operação consecutiva serão:
#
#     (0, 0, 1, 0, 0)
#     (0, 0, 1, 1, 0)
#     (0, 0, 1, 2, 0)
#     (2, 2, 2, 2, 2)
#     (3, 2, 2, 2, 2)
#     (3, 2, 2, 3, 2)
#     (3, 2, 2, 4, 2)
# O objetivo é calcular o valor de cada contador após todas as operações.
#
# Escreva uma função:
#
# solução def (N, A)
#
# que, dado um número inteiro N e uma matriz não vazia A que consiste em M números inteiros, retorna uma
# sequência de números inteiros representando os valores dos contadores.
#
# A matriz de resultados deve ser retornada como uma matriz de números inteiros.
#
# Por exemplo, dado:
#
#     A [0] = 3
#     A [1] = 4
#     A [2] = 4
#     A [3] = 6
#     A [4] = 1
#     A [5] = 4
#     A [6] = 4
# a função deve retornar [3, 2, 2, 4, 2], conforme explicado acima.
#
# Escreva um algoritmo eficiente para as seguintes suposições:
#
# N e M são números inteiros dentro do intervalo [1..100.000];
# cada elemento da matriz A é um número inteiro dentro do intervalo [1..N + 1].

A = [2, 3, 5, 4, 1, 2, 4, 3, 1, 5, 4, 3, 2, 2, 3, 1, 4, 2, 4, 1]
N = 5

def solution(N, A):
    lista = [0] * N

    for soma in A:
        try:
            lista[soma] += 1
            print('salve')

        except IndexError:
            maior_valor = max(lista)
            for i in range(len(lista)):
                lista[i] = maior_valor
                continue

    return lista

print(solution(N, A))


def solution(N, A):
    lista = []


    for i in A:
        posicao = i - 1
        if posicao < N:
            lista[posicao] += 1

        else:
            maior_valor = max(lista)
            for b in range(N):
                lista[b] = maior_valor

    return lista

def solution(N, A):
    pass