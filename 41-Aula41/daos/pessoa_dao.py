class PessoaDao:
    def listar_todos(self):
        return f'Listando todos os itens da tabela'

    def buscar_por_id(self, id):
        return f'Buscando objeto com id: {id}'

    def cadastrar(self, pessoa):
        return f'Criando um novo cadastro.'

    def alterar(self, pessoa):
        return f'Alterando um cadastro'

    def deletar(self, id):
        return f'Deletando cadastro de id:{id}'
