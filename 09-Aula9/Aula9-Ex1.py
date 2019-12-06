# Aula 9 - 19-11-2019
#--- Crie um programa que:
#--- 1-Leia dois números inteiros
#--- 2-Calcule a soma entre os dois números através de um método#---
#--- 3-Calcule a subtração entre os dois números através de um método
#--- 4-Calcule a multiplicação entre os dois números através de um método
#--- 5-Calcule a divisão inteira entre os dois números através de um método
#--- 6-Calcule a divisão fracionada entre os dois números através de um método
#--- 7-Calcule o resto da divisão entre os dois números através de um método
#--- 8-Calcule a raiz entre os dois números através de um método
#--- 9-Separe os métodos em outro arquivo


from calculos import calculo_soma, calculo_sub, calculo_mult, calculo_divint, calculo_divfrac, calculo_restodiv, calculo_raiz

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

r1 = calculo_soma(n1, n2)
print(f'A soma entre {n1} e {n2} é: {r1}')

r2 = calculo_sub(n1, n2)
print(f'A subtração entre {n1} e {n2} é: {r2}')

r3 = calculo_mult(n1, n2)
print(f'A multiplicação entre {n1} e {n2} é: {r3}')

r4 = calculo_divint(n1, n2)
print(f'A divisão inteira entre {n1} e {n2} é: {r4}')

r5 = calculo_divfrac(n1, n2)
print(f'A divisão fracionada entre {n1} e {n2} é: {r5}')

r6 = calculo_restodiv(n1, n2)
print(f'O resto da divisão entre {n1} e {n2} é: {r6}')

r7 = calculo_raiz(n1, n2)
print(f'A raiz entre {n1} e {n2} é: {r7}')
