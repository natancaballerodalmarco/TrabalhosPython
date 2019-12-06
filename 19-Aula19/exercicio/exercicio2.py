# Learn more or give us feedback
# Aula 19 - 04-12-2019
# Lista com for e metodos

cab = ['nome', 'telefone', 'email','idade']

pess   = [  ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
            ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
            ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
            ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'18'     ]   
        ]

# 1 - Usando estas 2 listas, fazer uma função que crie retorne uma lista com dicionários
# com os dados das pessoas com idade maior ou igua a 18 anos
print('='*100, '\n1-')

lista_maiores = []
for islow in range(7):
        dic = {}
        for ifast in range(4):
                dic[cab[ifast]] = pess[ifast][islow]
        if int(pess[3][islow]) >= 18:
                lista_maiores.append(dic)
print(lista_maiores)


#  2 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (não prescisa usar o f-string, .format())
print('\n', '='*100, '\n2-')

for dicionario in lista_maiores:
        print(dicionario)


#  3 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (usando o f-string)
print('\n', '='*100, '\n3-')

for i in range(len(lista_maiores)):
        print(f'{lista_maiores[i]}')

print('\n', '='*100)
