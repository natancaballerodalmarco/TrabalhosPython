class Calculadora:
    #-- Variável que nao pode ser alterada fora da classe(self no init + dois underline + variável
    def __init__(self, numero1, numero2, numero3):
        self.__n1 = numero1
        self.__n2 = numero2
        self.__n3 = numero3
        self.__resultado = 0

    #-- Opções para obter o resultado fora da Classe
    def soma(self):
        self.__resultado = self.__n1 + self.__n2
        return self.__resultado

    def subtracao(self):
        self.__resultado = self.__n1 - self.__n2 - self.__n3


    def multiplicacao(self):
        self.__resultado = self.__n1 * self.__n2 * self.__n3


    #-- Métodos Getters and Setters
    def set_n1(self, valor):
        self.__n1 = valor

    def set_n2(self, valor):
        self.__n2 = valor

    def set_n3(self, valor):
        self.__n3 = valor

    def get_n1(self):
        return self.__n1

    def get_n2(self):
        return self.__n2

    def get_n3(self):
        return self.__n3

    def get_resultado(self):
        return self.__resultado


#-- Instanciando um objeto da classe Calculadora
c = Calculadora(10, 20, 30)
print(c.get_n1())
print(c.get_n2())
print(c.get_n3())

c.set_n1(1000)
c.set_n2(2000)
c.set_n3(3000)

print(c.get_n1())
print(c.get_n2())
print(c.get_n3())

c.soma()
print(c.soma())
