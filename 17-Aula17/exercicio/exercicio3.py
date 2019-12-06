#Faça um programa para ler um número inteiro de 1 a 10
#Sorteie um número aleatório
#Diga se o número digitado é maior, menor ou igual
#Se o número digitado for igual encerre o programa

from random import randint
aleatorio = randint(1,10)
sorteio = 0

while True:
    sorteio = int(input('Para participar do sorteio digite um número inteiro ente 1 e 10: '))
    if 10 < sorteio or sorteio < 1:
        print('Digite um caractere válido!!!')
    elif sorteio < aleatorio:
        print('O número que você digitou é menor que o sorteado, tente novamente!\n')
    elif sorteio > aleatorio:
        print('O número que você digitou é maior que o sorteado, tente novamente!\n')
    elif sorteio == aleatorio:
        print('Parabéns, você acertou!')
    else:
        print('Digite um caractere válido!!!')

    