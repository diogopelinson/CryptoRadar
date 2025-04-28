from flask import render_template, request
import requests
from main import app

# Rota Dashboard
@app.route('/')
def index():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,cardano&vs_currencies=usd,brl'
    response = requests.get(url)
    dados = response.json()  # Obtendo os dados da API
    return render_template("index.html", dados=dados)

# Rota de Login
@app.route('/login')
def login():
    return render_template("login.html")

# Rota de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return render_template("cadastro.html", name=name, email=email)
    return render_template("cadastro.html")

# Rota de Cryptoia
@app.route('/cryptoia')
def cryptoia():
    return render_template("cryptoia.html")

