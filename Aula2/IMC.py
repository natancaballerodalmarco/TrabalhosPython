nome = input('Qual o seu nome? ')
sigin = int(input(f'Olá {nome}, para calcular seu IMC digite 1:'))

if sigin==1:
    n1 = float(input('Qual o seu peso? '))
    n2 = float(input('Qual a sua altura? '))
    c = int(n1 / (n2*n2))
    print(f'Sua massa corpórea é: {c:.2f}')
    if c< 17:
        print(f'Já ouviu falar em carne o seu vegano do car***? Você está muito abaixo do peso {nome}!!')
    elif c<= 18.5:
        print(f'É melhor comer um pouco mais, você está um pouco abaixo do peso {nome}.')
    elif c<= 25:
        print(f'Parabéns, você está em ótima forma {nome}!!')
    elif c<= 30:
       print(f'Você está um pouquinho acima do peso {nome}!')
    elif c<=35:
       print('Tome cuidado garotão, você já está com obesidade 1!!')
    elif c<=40:
       print('A obesidade 2 é muito perigosa!')
    elif c:
       print('Procure um médico, você está em um caso grave de obesidade 3!!!')
else:
    print('Obrigado, volte quando quiser.')