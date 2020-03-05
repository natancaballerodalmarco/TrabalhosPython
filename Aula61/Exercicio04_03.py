# Esta é uma tarefa de demonstração.
#
# Escreva uma função:
#
# solução def (A)
#
# que, dada uma matriz A de N números inteiros, retorna o menor número inteiro positivo (maior que 0) que não ocorre em A.
#
# Por exemplo, dado A = [1, 3, 6, 4, 1, 2], a função deve retornar 5.
#
# Dado A = [1, 2, 3], a função deve retornar 4.
#
# Dado A = [−1, −3], a função deve retornar 1.
#
# Escreva um algoritmo eficiente para as seguintes suposições:
#
# N é um número inteiro dentro do intervalo [1..100.000];
# cada elemento da matriz A é um número inteiro dentro do intervalo [-1.000.000..1.000.000].

A = [ 3, 6, 4, -50, -1000000, 1000000, 100000, -100000]


def solution(A):
    set1 = set(A)
    lista_organizada = list(set1)
    lista_organizada.sort()

    if 1 in lista_organizada:
        index = lista_organizada.index(1)
        for i in range(index, len(lista_organizada)):

            try:
                atual = lista_organizada[i]
                proximo = lista_organizada[i + 1]

                if atual + 1 != proximo:
                    return atual + 1

                else:
                    continue

            except IndexError:
                return lista_organizada[i] + 1
    return 1

print(solution(A))