class EnderecoModel:
    def __init__(self, nome, cidade, bairro, logradouro, numero, complemento, id=None):
        self.id = id
        self.nome = nome
        self.cidade = cidade
        self.bairro = bairro
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
