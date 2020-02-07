from Aula53.dao.pessoa_dao import PessoaDao
from Aula53.dao.endereco_dao import EnderecoDao

endao = EnderecoDao()
enderecos = endao.list_all()
dao = PessoaDao()
pessoas = dao.list_all()

print(pessoas)
for p in pessoas:
    print(p)

for e in enderecos:
    print(e)