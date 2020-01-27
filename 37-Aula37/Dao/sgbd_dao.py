import MySQLdb
from Model.sgbd import SGBD


class SGBDDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans01', user='padawans01', passwd='nn2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM SGBD"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM SGBD WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, sgbd:SGBD):
        comando = f""" INSERT INTO SGBD
        (
            Nome
        )
        VALUES
        (
            '{sgbd.Nome}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, sgbd:SGBD):
        comando = f""" UPDATE SGBD
        SET
            Nome = '{sgbd.Nome}'
        WHERE ID = {sgbd.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM SGBD WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()
