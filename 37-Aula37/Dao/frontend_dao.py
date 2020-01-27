import MySQLdb
from Model.frontend import FrontEnd


class FrontEndDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans01', user='padawans01', passwd='nn2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM FrontEnd"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM FrontEnd WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, frontend:FrontEnd):
        comando = f""" INSERT INTO FrontEnd
        (
            Nome
        )
        VALUES
        (
            '{frontend.nome}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, frontend:FrontEnd):
        comando = f""" UPDATE FrontEnd
        SET
            Nome = '{frontend.nome}'
        WHERE ID = {frontend.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM FrontEnd WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()
