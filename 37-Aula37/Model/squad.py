class Squad:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao = ''
        self.numeropessoas = 0
        self.linguagembackend = ''
        self.frameworkfrontend = ''
    
    def __Str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numeropessoas};{self.linguagembackend};{self.frameworkfrontend}'
