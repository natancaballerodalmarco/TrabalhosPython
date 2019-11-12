nome = input('Digite seu nome: ')
#print(nome)
sobrenome = input('Digite seu sobrenome: ')
#print(sobrenome)
idade = int(input('Digite sua idade: '))

print(f'seu nome completo é {nome} {sobrenome}')
if idade< 18:
    print('Você ainda é jovem, aproveite sua vida!')
elif idade< 59:
    print('Você já é adulto, deve estar no auge de sua vida!')
else:
    print('Você já é idoso, muitas histórias para contar...hehe')