class Endereco:
    id = 0
    cidade = ''
    bairro = ''
    logradouro = ''
    numero = 0
    complemento = ''

    def exportar_txt(self, lista_enderecos):
        with open('C:/Users/900154/Desktop/Python/TrabalhosPython/34-Aula34/Aula34-Endereco/enderecos.txt','a') as arquivo:
            for e in lista_enderecos:
                arquivo.write(f"{str(e)}\n")
    
    def __str__(self):
        return f'{self.id};{self.cidade};{self.bairro};{self.logradouro};{self.numero};{self.complemento}'
