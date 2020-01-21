import MySQLdb
import sys
sys.path.append('C:/Users/900154/Desktop/Python/TrabalhosPython/37-Aula37')
from Model.squad import Squad


class SquadDao:
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()

    def ler_todos(self):
        comando = f"SELECT * FROM Natan_Squad"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_id(self, id):
        comando = f"SELECT * FROM Natan_Squad WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado
    
    def salvar(self, squad = Squad):
        comando = f"""INSERT INTO Natan_Squad
        (
            Nome,
            Descricao,
            NumeroPessoas,
            LinguagemBackEnd,
            FrameworkFrontEnd
        )
        VALUES
        (
            '{squad.nome}',
            '{squad.descricao}',
            '{squad.numeropessoas}',
            '{squad.linguagembackend}',
            '{squad.frameworkfrontend}'
        )
        """
        self.cursor.execute(comando)
        self.cursor.commit()

