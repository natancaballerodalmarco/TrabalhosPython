# Criar uma classe cliente

# 1- Atributos: codigo, cpf, nome, idade, sexo

# 2- Métodos: receber salario, comprar

#  Quando recebe o salário aumenta o dinheiro na carteira
#  Quando compra aumenta os bens e diminui o dinheiro na carteira
#  Se comprar e não tiver dinheiro suficiente deve diminuir o dinheiro na carteira e aumentar a divida
#  Para pagar a divida tem que ter dinheiro suficiente na carteira

# 3- Estado: dinheiro na carteira, divida, bens


class Pessoa:
    
    def __init__(self):
        self.codigo = 1
        self.cpf = 12345678989
        self.nome = 'Jorje'
        self.sexo = 'M'
        self.carteira = 0
        self.divida = 0
        self.bens = 0
    
    def saldo (self, salario, compra, bens):
        self.carteira += salario
        self.divida += compra
        self.bens += bens

        if self.divida < self.carteira:
            self.carteira = self.carteira - self.divida
            self.divida = 0
            print(f'Você possui {self.carteira} reais na carteira')
            print(f'Você deve {self.divida} reais')
            print(f'Você possui {self.bens} bens')

        elif self.divida > self.carteira:
            self.divida = self.divida - self.carteira
            self.carteira = 0
            print(f'Você possui {self.carteira} reais na carteira')
            print(f'Você deve {self.divida} reais')
            print(f'Você possui {self.bens} bens')

        else:
            print(f'Você possui {self.carteira} reais na carteira')
            print(f'Você deve {self.divida} reais')
            print(f'Você possui {self.bens} bens')


a = 'b'
p = Pessoa()
while a != 'a':
    a = input('Se você deseja parar, digite "a": ')
    salario = float(input('Digite o salário: '))
    compra = float(input('Digite o valor gasto em compras: '))
    bens = int(input('Digite a quantidade de coisas compradas: '))
    p.saldo(salario, compra, bens)

print(p.codigo)
print(p.cpf)
print(p.nome)
print(p.sexo)
print(p.carteira)
print(p.divida)
print(p.bens)
