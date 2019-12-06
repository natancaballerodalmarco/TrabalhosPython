# Aula 10 - 20-11-2019

#--- Web - Calculadora
nome_pagina = 'Calculadora'
from flask import Flask, render_template, request
from calculos import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo=nome_pagina)

@app.route('/calcular')
def calcular():
    n1 = int(request.args['numero1'])
    n2 = int(request.args['numero2'])
    soma = calculo_soma(n1, n2)
    subtracao = calculo_sub(n1, n2)
    multiplicacao = calculo_mult(n1, n2)
    divisao_inteira = calculo_divint(n1, n2)
    divisao_fracionada = calculo_divfrac(n1, n2)
    resto = calculo_restodiv(n1, n2)
    raiz = calculo_raiz(n1, n2)
    resultados={'soma':soma, 'subtracao':subtracao, 'multiplicacao':multiplicacao, 'divisao_inteira':divisao_inteira, 'divisao_fracionada':divisao_fracionada, 'resto':resto, 'raiz':raiz}

    return render_template('resultado.html',
    n1 = n1,
    n2 = n2,
    resultados = resultados)

app.run()
