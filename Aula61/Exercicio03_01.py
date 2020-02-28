# Um sapo pequeno quer chegar ao outro lado da estrada. O sapo está atualmente localizado na posição X e deseja chegar a uma posição maior ou igual a Y.
# O sapo pequeno sempre pula uma distância fixa, D.
#
# Conte o número mínimo de saltos que o sapo pequeno deve realizar para atingir seu objetivo.
#
# Escreva uma função:
#
# solução def (X, Y, D)
#
# que, dados três números inteiros X, Y e D, retorne o número mínimo de saltos da posição X para uma posição igual ou superior a Y.
#
# Por exemplo, dado:
#
#   X = 10
#   Y = 85
#   D = 30
# a função deve retornar 3, porque o sapo será posicionado da seguinte maneira:
#
# após o primeiro salto, na posição 10 + 30 = 40
# após o segundo salto, na posição 10 + 30 + 30 = 70
# após o terceiro salto, na posição 10 + 30 + 30 + 30 = 100
# Escreva um algoritmo eficiente para as seguintes suposições:
#
# X, Y e D são números inteiros dentro do intervalo [1..1.000.000.000];
# X ≤ Y.

def solution(X, Y, D):
    distance = Y - X
    jumps = distance // D
    if distance % D > 0:
        jumps += 1
    return jumps
