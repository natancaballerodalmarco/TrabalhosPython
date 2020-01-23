import MySQLdb

conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans01', user='padawans01', passwd='nn2019')
cursor = conexao.cursor()
comando = ("SELECT * FROM Squads")
cursor.execute(comando)

for row in cursor.fetchall():
   print(f"""
ID: {row[0]},
Nome: {row[1]},
Descricao: {row[2]},
NumeroPessoas: {row[3]},
LinguagemBackEnd: {row[4]},
LinguagemFrontEnd: {row[5]}
""")