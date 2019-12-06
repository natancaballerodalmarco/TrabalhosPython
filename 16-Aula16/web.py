from flask import Flask, render_template

app = Flask(__name__)

@app.route('/lista')
def listar_faixas():
    return render_template("lista.html", nome = 'Lista de Faixas')

app.run()
