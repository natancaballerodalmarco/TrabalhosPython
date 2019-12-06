# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 
print('\n', '='*100, '\n1-')
cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]

cab = cadastroHBSIS[0::2]
dados = cadastroHBSIS[1::2]

# nome  Alex telefone: 4799991
# idade Carlos é 15 anos
# email de Mateus é d@d.com
print(f"{cadastroHBSIS[0]}: {cadastroHBSIS[1][0]}| {cadastroHBSIS[2]}: {cadastroHBSIS[3][0]}\n {cadastroHBSIS[6]} {cadastroHBSIS[1][4]} é {cadastroHBSIS[7][4]} anos \n{cadastroHBSIS[4]} de {cadastroHBSIS[1][3]} é {cadastroHBSIS[5][3]}")


# 2 - usando o for, imprima todos nomes um abaixo do outro
print('\n', '='*100, '\n2-')
for nome in dados[0]:
    print(nome)


# 3 - Usando a indexação faça uma lista com 3 dicionario contendo os dados do Mateus, Paulo e João
#  contendo como chaves: nome, email, idade, telefone (nesta  sequencia)
print('\n', '='*100, '\n3-')
lista = []

dicionario = {'nome':dados[0][3], 'email':dados[1][3], 'idade':dados[2][3], 'telefone':dados[3][3]}
lista.append(dicionario)
dicionario = {'nome':dados[0][1], 'email':dados[1][1], 'idade':dados[2][1], 'telefone':dados[3][1]}
lista.append(dicionario)
dicionario = {'nome':dados[0][5], 'email':dados[1][5], 'idade':dados[2][5], 'telefone':dados[3][5]}
lista.append(dicionario)
    
print(lista)
