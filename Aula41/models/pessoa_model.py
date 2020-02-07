from Aula41.models.endereco_model import EnderecoModel

class PessoaModel:

    def __init__(self, nome, sobrenome, idade, id=None):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        # self.endereco = EnderecoModel()
        # self.endereco.id = endereco_id
        # self.endereco.cidade = endereco_cidade
        # self.endereco.bairro = endereco_bairro
        # self.endereco.logradouro = endereco_logradouro
        # self.endereco.numero = endereco_numero
        # self.endereco.complemento = endereco_complemento
