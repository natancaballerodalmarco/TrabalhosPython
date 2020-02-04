class EnderecoModel:
    def __init__(self, cidade, bairro, logradouro, numero, complemento, id=None):
        self.id = id
        self.cidade = cidade
        self.bairro = bairro
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
