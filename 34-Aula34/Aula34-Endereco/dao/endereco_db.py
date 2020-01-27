import sys
sys.path.append('C:/Users/900154/Desktop/Python/TrabalhosPython/34-Aula34/Aula34-Endereco')
import MySQLdb
from model.endereco import Endereco

class EnderecoDb:
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()
    
    def listar_todos(self):
        comando_sql_select = "SELECT * FROM Natan_Endereco"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchall()
        lista_enderecos_classe = self.converter_tabela_classe(resultado)
        return lista_enderecos_classe

    def buscar_por_id(self, id):
        comando_sql_select = f"SELECT * FROM Natan_Endereco WHERE ID= {id}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado

    def converter_tabela_classe(self, lista_tuplas):
        lista_enderecos = []
        for e in lista_tuplas:
            e1 = Endereco()
            e1.id = e[0]
            e1.cidade = e[1]
            e1.bairro= e[2]
            e1.logradouro = e[3]
            e1.numero = e[4]
            e1.complemento = e
            lista_enderecos.append(e1)
        return lista_enderecos
