import MySQLdb

def listar_todos():
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()
    comando_sql_select = "SELECT * FROM Natan_Endereco"
    cursor.execute(comando_sql_select)
    resultado = cursor.fetchall()
    return resultado
