def calculo_montante(investimento, tempo, juros):
    porcentagem_juros = juros * 0.01
    mes = 0
    while mes < tempo:
        investimento = investimento + (investimento * porcentagem_juros)
        mes = (mes + 1)
    return investimento
