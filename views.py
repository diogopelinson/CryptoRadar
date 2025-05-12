from flask import render_template, request, session, redirect, flash, url_for
from utils.helpers import FormularioUsuario
from database.models import Usuarios
from main import app
from flask_bcrypt import check_password_hash
import requests

# Rota Dashboard
@app.route('/')
def index():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,cardano&vs_currencies=usd,brl'
    response = requests.get(url)
    dados = response.json()  
    return render_template("index.html", dados=dados)

# Rota de Login
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)


#Rota de Autenticar 
@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(usuario=form.usuario.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        session['usuario_logado'] = usuario.usuario
        flash(usuario.usuario + ' logado com sucesso')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuário não encontrado!')
        return redirect(url_for('login'))
    

#Rota de logout
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


# Rota de Cryptoia
@app.route('/cryptoia')
def cryptoia():
    return render_template("cryptoia.html")

