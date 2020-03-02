# Um sapo pequeno quer chegar ao outro lado de um rio. O sapo está inicialmente localizado em uma margem do rio (posição 0) e deseja chegar à margem
# oposta (posição X + 1). As folhas caem de uma árvore na superfície do rio.
#
# Você recebe uma matriz A que consiste em N números inteiros representando as folhas que caem. A [K] representa a posição em que uma folha
# cai no tempo K, medida em segundos.
#
# O objetivo é encontrar o primeiro momento em que o sapo possa pular para o outro lado do rio. O sapo pode atravessar apenas quando as folhas aparecem
# em todas as posições do rio, de 1 a X (ou seja, queremos encontrar o momento inicial em que todas as posições de 1 a X são cobertas por folhas). Você pode supor que a velocidade da corrente no rio é insignificante, ou seja, as folhas não mudam de posição quando caem no rio.
#
# Por exemplo, você recebe o número inteiro X = 5 e a matriz A de modo que:
#
#   A [0] = 1
#   A [1] = 3
#   A [2] = 1
#   A [3] = 4
#   A [4] = 2
#   A [5] = 3
#   A [6] = 5
#   A [7] = 4
# No segundo 6, uma folha cai na posição 5. É a primeira vez que as folhas aparecem em todas as posições do outro lado do rio.
#
# Escreva uma função:
#
# solução def (X, A)
#
# que, dada uma matriz não vazia A que consiste em N números inteiros e número inteiro X, retorna o primeiro tempo em que o sapo pode pular para o outro lado do rio.
#
# Se o sapo nunca for capaz de pular para o outro lado do rio, a função deve retornar -1.
#
# Por exemplo, dado X = 5 e matriz A de modo que:
X = 5
A = [1, 3, 1, 2, 2, 3, 5, 4]
# a função deve retornar 6, conforme explicado acima.
#
# Escreva um algoritmo eficiente para as seguintes suposições:
#
# N e X são números inteiros dentro do intervalo [1..100.000];
# cada elemento da matriz A é um número inteiro dentro do intervalo [1..X].

def solutiona(X, A):
    try:
        soma = (1 + X) * (X / 2)


        soma2 = 0
        folha = 0
        while soma2 < soma:
            verificacao = A[:folha]
            if not A[folha] in verificacao:
                soma2 += A[folha]
                print(soma2)
            folha += 1
        return folha - 1

    except IndexError:
        return -1

def solution(X, A):
    set1 = set()
    for indice, valor in enumerate(A):
        set1.add(valor)
        if len(set1) == X:
            return indice
    return -1

print(solution(X,A))