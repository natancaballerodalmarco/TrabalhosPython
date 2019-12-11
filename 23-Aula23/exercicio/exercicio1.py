# For para Dicionário

dias_do_mes = {
    1: 31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

qual_mes = int(input('Digite o número do mês(1,12): '))

print(f'O mês {qual_mes} tem {dias_do_mes[qual_mes]}')
print('Dias faltantes para acabar o ano, a partir do mês informado: ')
print(sum(list(dias_do_mes.values())[qual_mes-1:]))

total = 0
for mes in range(qual_mes, 13):
    total += dias_do_mes[mes]
print('modo estruturado')
print(f'total de dias até o fim do ano {total}')

print('='*150,'\n')

for chave in dias_do_mes:
    print('tenho uma chave nessa linha', chave)
    print('Se tenho a chave, tenho o valor', dias_do_mes[chave])

print('='*150,'\n')

for chave, valor in dias_do_mes.items():
    print(f'Para a chave{chave}, o valor é {valor}')

print('='*150,'\n')

tupla = ('Texto', 42, 5.05, int, str, list)

for isto in tupla:
    print(type(isto))
    print(isto)