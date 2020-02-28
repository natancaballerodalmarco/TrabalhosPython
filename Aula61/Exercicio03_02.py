# É fornecida uma matriz A que consiste em N números inteiros diferentes. A matriz contém números inteiros no intervalo [1 .. (N + 1)],
#o que significa que exatamente um elemento está ausente.
#
# Seu objetivo é encontrar esse elemento que está faltando.
#
# Escreva uma função:
#
# solução def (A)
#
# que, dada uma matriz A, retorna o valor do elemento ausente.
#
# Por exemplo, dada a matriz A de modo que:
#
#   A [0] = 2
#   A [1] = 3
#   A [2] = 1
#   A [3] = 5
# a função deve retornar 4, pois é o elemento que falta.
#
# Escreva um algoritmo eficiente para as seguintes suposições:
#
# N é um número inteiro dentro do intervalo [0..100.000];
# os elementos de A são todos distintos;
# cada elemento da matriz A é um número inteiro dentro do intervalo [1 .. (N + 1)].

A = [3, 2, 5, 1]

def solution(A):
    try:
        if len(A) == 0:
            return 1

        A = sorted(A)
        for i in range(len(A)):

            if A[i+1] - A[i] == 2:
                return (A[i] + 1)

    except IndexError:

        if A[0] != 1:
            return 1

        elif len(A) == 1:
            resultado = A[0]
            return resultado + 1


        else:
            resultado = A[-1]
            return resultado + 1

print(solution(A))