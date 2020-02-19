#-- Verifica se determinada condição é verdadeira
from Aula59.A59 import subtracao

assert True
assert (10 == 10)
assert (10 > 5)
assert ('Natan' != "Nathan")



def soma(n1, n2):
    resultado = n1 + n2
    return resultado

def multiplicacao(n1, n2, n3=1):
    resultado = n1 * n2 * n3
    return resultado

def checa_maioridade(idade):
    if idade > 17:
        return True
    else:
        return False

assert soma(5, 10) == 15
assert multiplicacao(2, 4, 6) == 48
assert multiplicacao(2, 4) == 8
assert checa_maioridade(17) == False
assert checa_maioridade(18) == True
assert checa_maioridade(19) == True
assert subtracao(10, 9, 8) < 0