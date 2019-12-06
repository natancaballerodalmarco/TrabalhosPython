print('='*50, '\n')

def salvar_cerveja(cerveja_dicionario):
    arquivo = open('aula15.txt', 'a')
    arquivo.write(f"{cerveja_dicionario['marca']}|{cerveja_dicionario['tipo']}|{cerveja_dicionario['teor']}\n")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('aula15.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split('|')
        cerveja = {'marca':lista_linha[0], 'tipo':lista_linha[1], 'teor':lista_linha[2]} 
        lista.append(cerveja)
    arquivo.close()
    return lista

marca = input('Digite a marca da cerveja: ')
tipo = (input('Digie seu tipo: '))
teor = (float(input('Digite seu teor alcoólico: ')))

cerveja = {'marca':marca, 'tipo':tipo, 'teor': teor}
salvar_cerveja(cerveja)

# arquivo = open('aula15.txt', 'a')
# arquivo.write(cerveja)
# arquivo.close()

print('\n', '='*50, '\n')
for c in ler():
    print(f"{c['marca']} - {c['tipo']} - {c['teor']}")

print('\n', '='*50)
