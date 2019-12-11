# #1 - Características da pessoa:
# # Atributos - Variáveis

# nome
# idade
# telefone
# sexo

# # Metodos
# respira
# dorme
# corre
# bebe
# come
# reproduz


# #3 - Como a pessoa está agora:
# # Atributos de estado - Variáveis
# divida
# cansada
# viva
# fome
# sede


class Pessoa:
    '''
    Esta classe é uma demonstrção para a aula
    '''
    def __init__(self, nome1, idade1, telefone1, sexo1):
        '''
        O __init__ é o motor que irá iniciar as variáveis da classe
        O self é o que irá conectar toda a classe
        '''
        # Atributos #### 
        self.nome = nome1
        self.idade = idade1
        self.telefone = telefone1
        self.sexo = sexo1
        #
        self.divida = None
        self.cansada = 'não'
        self.viva = True
        self.fome = 'não'
        self.sede = 'não'

    # Metodos ###
    def respira (self, respirar):
        if self.viva == True:
            if respirar == True:
                self.viva = True
            else:
                self.viva = False
        
    def corre (self, distancia):
        if self.viva:
            if 100 > distancia:
                self.cansada = 'pouco'
                self.sede = 'pouco'
                self.fome = 'pouco'

            elif distancia >=100 and distancia <200:
                self.cansada = 'medio'
                self.sede = 'medio'
                self.fome = 'medio'

            else:
                self.cansada = 'muito'
                self.sede = 'muito'
                self.fome = 'muito'

    def dorme (self):
        if self.viva:
            self.cansada = 'não'
            self.fome = 'não'
            self.sede = 'não'

    def bebe (self):
        if self.viva:
            self.sede = 'não'

    def come (self):
        if self.viva:
            self.fome = 'não'

    # def reproduz (self):
    #     if self.viva:
    #         self.reproduz = 'sim'





p = Pessoa('Natan', 18, '47920003333', 'm')
p.corre(150)
p.dorme()
# p.come()
# p.bebe()

print(f'Nome é {p.nome}')
print(f'Está vivo? {p.viva}')
print(f'Está com fome? {p.fome}')
print(f'Está com sede? {p.sede}')
print(f'Está cansada? {p.cansada}')

arquivo = open()
arquivo.write()
