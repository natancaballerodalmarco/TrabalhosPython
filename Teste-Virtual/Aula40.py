from flask import Flask
from flask_restful  import

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem vindo a API'

if __name__ == '__main__':
    app.run(debug=True, port=80)
