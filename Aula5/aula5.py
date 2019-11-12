n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
m = float((n1 + n2 + n3 + n4) / 4)

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n4 > maior:
    maior = n4
print(f'A maior nota é {maior}')

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4
print(f'A menor nota é {menor}')

print(f'A média é {m}')
if m > 7:
    print('Você foi aprovado!!')
else:
    print('Você foi reprovado!')
