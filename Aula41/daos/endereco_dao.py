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
        endereco = self.cursor.fetchone()
        end = EnderecoModel(endereco[1], endereco[2], endereco[3], endereco[4], endereco[5], endereco[0])

        return end.__dict__


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
