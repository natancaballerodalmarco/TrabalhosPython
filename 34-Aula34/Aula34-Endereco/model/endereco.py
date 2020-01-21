class Endereco:
    id = 0
    cidade = ''
    bairro = ''
    logradouro = ''
    numero = 0
    complemento = ''

    def exportar_txt(self, lista_enderecos):
        with open('enderecos.txt','a') as arquivo:
            for e in lista_enderecos:
                arquivo.write(f"{(e)}\n")
    
    def __str__(self):
        return f'{self.id};{self.cidade};{self.bairro};{self.logradouro};{self.numero};{self.complemento}'
