lista = []
dicionario = { 'Nome':'Natan', 'Sobrenome':'Caballero'}
print(dicionario)
print(dicionario['Sobrenome'])

nome = 'Mateus'
lista_notas = [10,20,50,70]
media = sum(lista_notas)/ len(lista_notas)
situacao = 'Reprovado'
if media >=7:
    situacao = 'Aprovado'
dicionario_alunos = {'Nome': nome, 'Lista_Notas': lista_notas, 'Media': media, 'Situacao':situacao}

print(f"{dicionario_alunos['Nome']} - {dicionario_alunos['Situacao']}")


#pode criar dicionario vazio e ir adicionando chaves

informacoes = {}
informacoes['telefone'] = 30303030
informacoes['beleza'] = 5/10
print(f"{informacoes['telefone']} | {informacoes['beleza']}")