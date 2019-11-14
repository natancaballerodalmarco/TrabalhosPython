# - Exercício 3 - Foreach
# - Escreva um programa que leia as notas (4) de 10 alunos
# - Armazene as notas e os nomes em lista:
# - Iprima:
#       1-O nome dos alunos
#       2-Suas respectivas médias 
#       3-Resultado(Aprovado>=7 ou Reprovado<7)
nomes = []
notas = []
a = 0
b = 1
c = 2
d = 3

for a in range(0,10):
    nomes.append(input(f'Nome de aluno {a+1}: '))
    for b in range(0,4):
        notas.append(float(input(f'Nota {b+1}: ')))

for aluno in nomes:
    media = (notas[a]+notas[b]+notas[c]+notas[d])/4
    print(f'\nNome: {aluno}')
    print(f'Média: {media}')
    if media >= 7:
        print('Aprovado!')
    else:
        print('Reprovado!')
a += 4
b += 4
c += 4
d += 4