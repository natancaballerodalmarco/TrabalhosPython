def converter_tabela_dicionario(lista_tuplas):
    lista_enderecos = []

    for p in lista_tuplas:
        dicionario_endereco = {'ID': 0, 'Cidade': '', 'Bairro': '', 'Logradouro': '', 'Numero': 0, 'Complemento': ''}
        dicionario_endereco['ID'] = p[0]
        dicionario_endereco['Cidade'] = p[1]
        dicionario_endereco['Bairro'] = p[2]
        dicionario_endereco['Logradouro'] = p[3]
        dicionario_endereco['Numero'] = p[4]
        dicionario_endereco['Complemento'] = p[5]
        lista_enderecos.append(dicionario_endereco)

    return lista_enderecos
