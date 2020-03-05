import math

assert True
# assert False
assert 2 == 2, 'não são dois números iguais'

def soma(x, y):
    resultado = x + y
    return resultado

assert soma(5, 5) == 10, 'a soma está incorreta'

class Natan:
    nome = ''
    idade = 0

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        self.idade = idade

pessoa01 = Natan()
assert isinstance(pessoa01, Natan), 'Não é uma instancia da classe pessoa'

pessoa01.set_nome('Natan')
assert pessoa01.get_nome() == 'Natan', 'Nome incorreto'



################################################# COM FRAMEWORK

print(math.fabs(5.55))

from math import sqrt