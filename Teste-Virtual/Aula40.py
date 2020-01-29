from flask import Flask
from flask_restful 

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem vindo a API'

app.run(debug=True, port=80)