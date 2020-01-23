import MySQLdb
from Model.squad import Squad

class SquadDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans01', user='padawans01', passwd='nn2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM Squads"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_id(self, id):
        comando = f"SELECT * FROM Squads WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado
    
    def salvar(self, squad = Squad):
        comando = f"""INSERT INTO Squads
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
            {squad.numeropessoas},
            '{squad.linguagembackend}',
            '{squad.frameworkfrontend}'
        )"""
        self.cursor.execute(comando)
        self.cursor.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, squad:Squad):
        comando = f""" UPDATE Squads
        SET
            Nome = '{squad.nome}',
            Descricao ='{squad.descricao}',
            NumeroPessoas = {squad.numeropessoas},
            LinguagemBackEnd = '{squad.linguagembackend}',
            FrameworkFrontEnd = '{squad.frameworkfrontend}'
        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM Squads WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()
