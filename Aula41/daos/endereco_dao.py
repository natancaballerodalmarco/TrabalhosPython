import MySQLdb

from Aula41.models.endereco_model import EnderecoModel

class EnderecoDao:

    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019')
        self.cursor = self.connection.cursor()


    def list_all(self):
        self.cursor.execute(f"SELECT * FROM Natan_Endereco ")
        enderecos = self.cursor.fetchall()

        lista_enderecos = []
        for e in enderecos:
            endereco = EnderecoModel(e[1], e[2], e[3], e[4], e[5], e[0])
            lista_enderecos.append(endereco.__dict__)

        return lista_enderecos


    def get_by_id(self,id):
        self.cursor.execute(f"SELECT * FROM Natan_Endereco WHERE ID = {id}")
        end = self.cursor.fetchone()

        endereco = EnderecoModel(end[1], end[2], end[3], end[4], end[5], end[0])

        return endereco.__dict__


    def insert(self, endereco:EnderecoModel):
        self.cursor.execute(f"""INSERT INTO Natan_Endereco
                                (
                                    Cidade,
                                    Bairro,
                                    Logradouro,
                                    Numero,
                                    Complemento
                                ) 
                                VALUES
                                (
                                    '{endereco.cidade}',
                                    '{endereco.bairro}',
                                    '{endereco.logradouro}',
                                    {endereco.numero},
                                    '{endereco.complemento}'
                                )""")

        self.connection.commit()
        id = self.cursor.lastrowid
        endereco.id = id

        return endereco.__dict__

    def update(self, endereco:EnderecoModel):
        self.cursor.execute(f"""UPDATE Natan_Endereco
                                SET
                                    Cidade = '{endereco.cidade}', 
                                    Bairro = '{endereco.bairro}', 
                                    Logradouro = '{endereco.logradouro}', 
                                    Numero = {endereco.numero}, 
                                    Complemento = '{endereco.complemento}'
                                WHERE ID = {endereco.id}
                                """)

        self.connection.commit()

        return endereco.__dict__

    def delete(self, id):
        self.cursor.execute(f"DELETE FROM Natan_Endereco WHERE ID = {id}")
        self.connection.commit()

        return f'Removido o endereco de id = {id}'

