import MySQLdb
from endereco_converter import converter_tabela_dicionario
from endereco_db import listar_todos
from endereco_export import exportar_txt

list_tup_endereco = listar_todos()
list_dic_endereco = converter_tabela_dicionario(list_tup_endereco)
exportar_txt(list_dic_endereco)
