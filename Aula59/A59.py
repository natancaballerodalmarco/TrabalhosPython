#-- Argumentos Ordenados:

def soma(n1, n2):
    resultado = n1+n2
    return resultado

res = soma(10, 20)
print(res)


def multiplicacao(n1, n2, n3):
    resultado = n1 * n2 * n3
    return resultado

res2 = multiplicacao(10, 20, 30)
print(res2)




#-- Argumentos Nomeados:

def subtracao(n1, n2, n3):
    resultado = n1 - n2 - n3
    return resultado

res3 = subtracao(n3=10, n2=20, n1=30)
print(res3)



#-- Argumentos Opcionais:

def multiplicacao2(n1, n2, n3=1):
    resultado = n1 * n2 * n3
    return resultado

res4 = multiplicacao2(10,20)
print(res4)