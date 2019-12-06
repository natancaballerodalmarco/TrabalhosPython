def calculo_montante(cotas, tempo):
    porcentagem_juros = 0.003
    investimento = cotas * 10410
    mes = 0
    while mes < tempo:
        investimento = investimento + (investimento * porcentagem_juros)
        mes = (mes + 1)
    return investimento
