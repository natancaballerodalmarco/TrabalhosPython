# Aula 16 - 28-11-2019
# ????????????
#cadastro de playlist
#lendo musica, artista e álbum

print('='*50, '\n')
from Faixa import criar_faixa, salvar_faixa, ler_faixa

musica = input('Digite uma musica: ')
album = input('Digite um album: ')
artista = input('Digite o nome do artista: ')

faixa = criar_faixa(musica, album, artista)
salvar_faixa(faixa)
lista = ler_faixa()

for faixa in lista:
    print(f"{faixa['musica']} - {faixa['album']} - {faixa['artista']}")

print('\n', '='*50)
