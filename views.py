from flask import render_template, request
from main import app, dados


# Rota Dashboard


@app.route('/')
def index():
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
