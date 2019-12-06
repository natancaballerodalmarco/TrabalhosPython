class FestaHBSIS:
    '''
    Classe que mcontrola a festa de arromba da HBSIS
    que acontece 1 vez por ano!!!
    '''

    def __int__(self):
        '''
        i __int__ é para iniciar as variáveis e 
        disponibilizá-la para todos os metodos da classe.
        '''
        self.lista = self.ler_cadastro()
    def ler_cadastro(self):
        arquivo = open('18-Aula18/exercicio/cadastro.txt', 'r')
        self.lista = []

        for pessoa in arquivo:
            pessoa = pessoa.strip().split('|')
            dicio = {'Codigo':pessoa[0], 'Nome':pessoa[1],
                    'Sexo':pessoa[2], 'Idade':pessoa[3]}
            self.lista.append(dicio)
        arquivo.close()
        return self.lista
    def lista_festa(self):
        lista_homens = []
        lista_mulheres = []

        for pessoa in self.lista:
            if int(pessoa['Idade']) >= 18:
                if pessoa['Sexo'] == 'F':
                    lista_mulheres.append(pessoa)
                else:
                    lista_homens.append(pessoa)

        salvar(lista_homens, 'homens')
        salvar(lista_mulheres, 'mulheres')
    def salvar(self, lista1, nome):
        arquivo = open(f'18-Aula18/exercicio/{nome}','a')
        for pessoa in lista1:
            texto = f"{pessoa['Codigo']}|{pessoa['Nome']}|{pessoa['Sexo']}|{pessoa['Idade']}\n"

            arquivo.write(texto)
                    
        arquivo.close()
    def consulta(lista_consulta_funcao, numero):
        for lista_consulta in lista_consulta_funcao:
            if int(lista_consulta['Codigo']) == numero:
                
                if int(lista_consulta['Idade']) >= 18:
                    if lista_consulta['Sexo'] == 'F':
                        print(f"Nome: {lista_consulta['Nome']}, Valor do ingresso: R$15.00 ")
                    else:
                        print(f"Nome: {lista_consulta['Nome']}, Valor do ingresso: R$35.00 ")
                else:
                    print('Não pode entrar!!!')
