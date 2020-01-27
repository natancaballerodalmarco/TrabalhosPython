import MySQLdb

conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans01', user='padawans01', passwd='nn2019')
cursor = conexao.cursor()

def listar_todos():
    comando = "SELECT * FROM Squads"
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado

def listar_todos01():
    lista_dicionarios = []
    lista_tuplas = listar_todos()
    for s in lista_tuplas:
        dicionario_squad = {'Id': 0, 'Nome' : '', 'Descricao': '', 'NumeroPessoas' : 0, 'LinguagemBackEnd': '', 'FrameworkFrontEnd': ''}
        dicionario_squad['Id'] = s[0]
        dicionario_squad['Nome'] = s[1]
        dicionario_squad['Descricao'] = s[2]
        dicionario_squad['NumeroPessoas'] = s[3]
        dicionario_squad['LinguagemBackEnd'] = s[4]
        dicionario_squad['FrameworkFrontEnd'] = s[5]
        lista_dicionarios.append(dicionario_squad)
    return lista_dicionarios

def salvar(squad):
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
    '{squad['Nome']}',
    '{squad['Descricao']}',
    {squad['NumeroPessoas']},
    '{squad['LinguagemBackEnd']}',
    '{squad['FrameworkFrontEnd']}'
)"""
    cursor.execute(comando)
    conexao.commit()

def editar(squad):
    comando = f""" UPDATE Squads
SET
    Nome = '{squad['Nome']}',
    Descricao = '{squad['Descricao']}',
    NumeroPessoas = {squad['NumeroPessoas']},
    LinguagemBackEnd = '{squad['LinguagemBackEnd']}',
    FrameworkFrontEnd = '{squad['FrameworkFrontEnd']}'
WHERE ID = {squad['Id']}
"""
    cursor.execute(comando)
    conexao.commit()

def deletar(id):
    comando = f"DELETE FROM Squads WHERE ID = {id}"
    cursor.execute(comando)
    conexao.commit()


# squad_novo = {'Nome' : 'HeadAches', 'Descricao': 'Só dor de cabeça', 'NumeroPessoas' : 6, 'LinguagemBackEnd': 'Python', 'FrameworkFrontEnd': 'JavaScript'}
# salvar(squad_novo)
# squad_editado = {'Id':12, 'Nome' : 'HeadAches', 'Descricao': 'Dor de cabeca', 'NumeroPessoas' : 6, 'LinguagemBackEnd': 'Python', 'FrameworkFrontEnd': 'JavaScript'}
# editar(squad_editado)
deletar(12)
print(listar_todos01())
