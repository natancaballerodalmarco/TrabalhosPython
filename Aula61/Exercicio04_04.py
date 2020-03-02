# Uma matriz não vazia A que consiste em N números inteiros é fornecida.
# Uma permutação é uma sequência que contém cada elemento de 1 a N uma vez e apenas uma vez.
# Por exemplo, matriz A de modo que:
#
#     A [0] = 4
#     A [1] = 1
#     A [2] = 3
#     A [3] = 2
# é uma permutação, mas a matriz A é tal que:
#
#     A [0] = 4
#     A [1] = 1
#     A [2] = 3
# não é uma permutação, porque o valor 2 está ausente.
# O objetivo é verificar se a matriz A é uma permutação.
# Escreva uma função:
# solução def (A)
# que, dada uma matriz A, retorna 1 se a matriz A for uma permutação e 0 se não for.
# Por exemplo, dada a matriz A de modo que:
A = [1, 2, 3, 5, 4]
# a função deve retornar 1.
#
# Dada matriz A, de modo que:
#
#     A [0] = 4
#     A [1] = 1
#     A [2] = 3
# a função deve retornar 0.
#
# Escreva um algoritmo eficiente para as seguintes suposições:
#
# N é um número inteiro dentro do intervalo [1..100.000];
# cada elemento da matriz A é um número inteiro dentro do intervalo [1..1.000.000.000].

def solution(A):
    set1 = {i for i in A}
    if len(set1) != len(A):
        return 0
    maior = max(set1)
    soma = 0
    pares = maior // 2
    if maior % 2 > 0:
        soma = (maior) * pares + maior
    else:
        soma = (1 + maior) * pares
    if sum(set1) == soma:
        return 1
    return 0

print(solution(A))
