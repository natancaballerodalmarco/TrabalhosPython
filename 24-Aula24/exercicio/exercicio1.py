# Aula 24 - 11-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:


# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)
print('='*150, '\n')


class Cliente:
    def __init__(self, dadobruto):
        self.dado_bruto = dadobruto
        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None

    def tratar_dado(self):
        pessoa = self.dado_bruto.strip().split(';')
        self.codigo = int(pessoa[0])
        self.nome = pessoa[1]
        self.idade = int(pessoa[2])
        self.sexo = pessoa[3]
        self.email = pessoa[4]
        self.telefone = pessoa[5]

    def __str__(self):
        texto = f'''
        Codigo: {self.codigo}
        Nome: {self.nome}
        Idade: {self.idade}
        Sexo: {self.sexo}
        E-mail: {self.email}
        Telefone: {self.telefone}
        '''
        return texto




    def __eq__(self,valor):
        return self.codigo == valor
         
dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

dado_bruto = dadobruto.split(';')
print(dado_bruto)

pess = []
pess.append(Cliente(dadobruto))
pess.tratar_dado()


print(f'Código: {pess.codigo}\nNome: {pess.nome}\nIdade: {pess.idade}\nSexo: {pess.sexo}\ne-mail: {pess.email}\nTelefone: {pess.telefone}')

print('\n', '='*150)

while True:
    var = int(input('Digite o código'))
    press[0 == 1]