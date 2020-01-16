def exportar_txt(lista_enderecos):
    with open('34-Aula34/enderecos.txt','a') as arquivo:
        for p in lista_enderecos:
            arquivo.write(f"{p['ID']};{p['Cidade']};{p['Bairro']};{p['Logradouro']};{p['Numero']};{p['Complemento']}\n")
