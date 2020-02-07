import MySQLdb

from Aula41.models.pessoa_model import PessoaModel
from Aula41.models.endereco_model import EnderecoModel

class PessoaDao:

    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019')
        self.cursor = self.connection.cursor()

    def list_all(self):
        self.cursor.execute("""
                            SELECT * FROM 
                            Natan_Pessoa as p LEFT JOIN Natan_Endereco as e
                            ON e.ID = p.Endereco_FK
                            """)
        pessoas = self.cursor.fetchall()

        lista_pessoa = []
        for p in pessoas:
            pessoa = PessoaModel(p[1], p[2], p[3], p[0])
            endereco = EnderecoModel(p[6], p[7], p[8], p[9], p[10], p[5])
            lista_pessoa.append(pessoa.__dict__)
            lista_pessoa.append(endereco.__dict__)

        return lista_pessoa

    def get_by_id(self, id):
        self.cursor.execute(f"""
                            SELECT * FROM 
                            Natan_Pessoa as p LEFT JOIN Natan_Endereco as e 
                            ON e.ID = p.Endereco_FK WHERE p.ID={id}
                            """)
        pessoa = self.cursor.fetchone()

        p = PessoaModel(pessoa[1], pessoa[2], pessoa[3], pessoa[0])

        return p.__dict__


    def insert(self, pessoa:PessoaModel):
        self.cursor.execute(f"""
                            INSERT INTO Natan_Pessoa
                                (Nome, Sobrenome, Idade) 
                            VALUES
                                ('{pessoa.nome}','{pessoa.sobrenome}',{pessoa.idade})
                            """)
        self.connection.commit()

        id = self.cursor.lastrowid
        pessoa.id = id

        return pessoa.__dict__


    def update(self, pessoa=PessoaModel):
        self.cursor.execute(f"""
                            UPDATE Natan_Pessoa
                            SET 
                                Nome = '{pessoa.nome}', 
                                Sobrenome = '{pessoa.sobrenome}', 
                                Idade = {pessoa.idade}
                            WHERE ID = {pessoa.id}
                            """)
        self.connection.commit()

        return pessoa.__dict__


    def delete(self, id):
        self.cursor.execute(f"""
                            DELETE FROM Natan_Pessoa 
                            WHERE ID={id}
                            """)
        self.connection.commit()

        return f'Removida a pessoa de id: {id}'
