print('='*50, '\n')

def salvar_pessoa(pessoa_dicionario):
    arquivo = open('aula15.txt', 'a')
    arquivo.write(f"{pessoa_dicionario['nome']}|{pessoa_dicionario['sobrenome']}|{pessoa_dicionario['idade']}\n")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('aula15.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split('|')
        pessoa = {'nome':lista_linha[0], 'sobrenome':lista_linha[1], 'idade':lista_linha[2]} 
        lista.append(pessoa)
    arquivo.close()
    return lista

# nome = input('Digite seu nome: ')
# sobrenome = (input('Digie seu sobrenome: '))
# idade = (int(input('Digite sua idade: ')))

# pessoa = {'nome':nome, 'sobrenome':sobrenome, 'idade': idade}
# salvar_pessoa(pessoa)

# arquivo = open('aula15.txt', 'a')
# arquivo.write(pessoa)
# arquivo.close()

for p in ler():
    print(f"{p['nome']} - {p['sobrenome']} - {p['idade']}")


print('\n', '='*50)
    