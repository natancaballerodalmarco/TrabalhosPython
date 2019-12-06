# Aula 18 - 03-11-2019

# Festa da HBSIS

# 1 - Faça uma função que leia do arquivo cadastro.txt e retorne uma lista com dicionários.
# cada linha possui os dados na seguinte posição: codigo, nome, sexo, idade

# 2 - Como a entrada da festa é mais barata para mulheres (R$ 15,00) do que para os homens (R$ 35,00) 
# deve-se separar os dois em duas listas separadas e salvar em arquivos separados. Como é uma festa de arromba,
# menores de idade não podem entrar.

# 3 - Faça uma terceira função que ao digitar o código do participante ele imprima o nome do participante, 
# o valor do ingresso, e em caso de menores de idade apareça o texto "Entrada Proibida!"

def ler_cadastro():
    arquivo = open('18-Aula18/exercicio/cadastro.txt', 'r')
    registros = []

    for pessoa in arquivo:
        pessoa = pessoa.strip().split('|')
        dicio = {'Codigo':pessoa[0], 'Nome':pessoa[1],
                 'Sexo':pessoa[2], 'Idade':pessoa[3]}
        registros.append(dicio)
    arquivo.close()
    return registros


def lista_festa(lista_de_entradas):
    lista_homens = []
    lista_mulheres = []

    for pessoa in lista_de_entradas:
        if int(pessoa['Idade']) >= 18:
            if pessoa['Sexo'] == 'F':
                lista_mulheres.append(pessoa)
            else:
                lista_homens.append(pessoa)

    salvar(lista_homens, 'homens')
    salvar(lista_mulheres, 'mulheres')


def salvar(lista, nome):
    arquivo = open(f'18-Aula18/exercicio/{nome}','a')
    for pessoa in lista:
        texto = f"{pessoa['Codigo']}|{pessoa['Nome']}|{pessoa['Sexo']}|{pessoa['Idade']}\n"

        arquivo.write(texto)
                
    arquivo.close()


def consulta(lista_consulta_funcao, numero):
    for lista_consulta in lista_consulta_funcao:
        if int(lista_consulta['Codigo']) == numero:
            
            if int(lista_consulta['Idade']) >= 18:
                if lista_consulta['Sexo'] == 'F':
                    print(f"Nome: {lista_consulta['Nome']}, Valor do ingresso: R$15.00 ")
                else:
                    print(f"Nome: {lista_consulta['Nome']}, Valor do ingresso: R$35.00 ")
            else:
                print('Não pode entrar!!!')


lista1 = ler_cadastro()
lista_festa(lista1)

while True:
    a = int(input('Digite o código: '))
    consulta(lista1,a)
