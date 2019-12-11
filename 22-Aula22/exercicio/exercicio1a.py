# Criar uma classe cliente

# 1- Atributos: codigo, cpf, nome, idade, sexo

# 2- Métodos: receber salario, comprar

#  Quando recebe o salário aumenta o dinheiro na carteira
#  Quando compra aumenta os bens e diminui o dinheiro na carteira
#  Se comprar e não tiver dinheiro suficiente deve diminuir o dinheiro na carteira e aumentar a divida
#  Para pagar a divida tem que ter dinheiro suficiente na carteira

# 3- Estado: dinheiro na carteira, divida, bens


class Pessoa:
    
    def __init__(self, codigo, cpf, nome, sexo):
        self.codigo = codigo
        self.cpf = cpf
        self.nome = nome
        self.sexo = sexo
        self.carteira = 
        self.divida = 
        self.bens = 
    
    def saldo (self, salario, compra, bens):
        self.carteira = self.carteira + salario
        self.divida = self.divida + compra
        self.bens = self.bens + bens

        if self.divida < self.carteira:
            self.carteira = self.carteira - self.divida
            self.divida = 0
            print(f'Você possui {self.bens} bens')
        else:
            print(f'Você possui {self.bens} bens')



p = Pessoa(0, 89452315789, 'Natan', 'M')
salario = float(input('Digite o salário: '))
compra = float(input('Digite o valor gasto em compras: '))
bens = float(input('Digite a quantidade de coisas compradas: '))
p.saldo(salario, compra, bens)

print(p.codigo)
print(p.cpf)
print(p.nome)
print(p.sexo)
print(p.carteira)
print(p.divida)
print(p.bens)
