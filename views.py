from flask import render_template, request, session, redirect, flash, url_for
from utils.helpers import FormularioUsuario, PerguntaForm
from database.models import Usuarios
from main import app, genai
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
@app.route('/cryptoia', methods=['GET', 'POST'])
def cryptoia():
    form = PerguntaForm()
    resposta = None

    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest') 


    except Exception as e:
        erro_msg = f"Erro de configuração da IA ou inicialização do modelo: {e}"
        print(erro_msg)
        flash(erro_msg + " Por favor, verifique a chave API e a configuração em main.py.", "danger")
        return render_template("cryptoia.html", form=form, resposta=None)


    if form.validate_on_submit():
        pergunta_usuario = form.pergunta.data
        
      
        persona_contexto = (
            "Você é um especialista altamente qualificado em Bitcoin e outras criptomoedas. "
            "Sua tarefa é responder a perguntas de forma **direta, concisa, informativa e precisa**. " 
            "Foque em conceitos técnicos, históricos, casos de uso e notícias relevantes. "
            "**EVITE enrolação ou respostas vagas.** Vá direto ao ponto. " 
            "Evite dar conselhos financeiros ou previsões de preços. "
            "Responda à seguinte pergunta:\n\n"
        )
        
        prompt_completo = persona_contexto + pergunta_usuario

        try:
            response = model.generate_content(
                prompt_completo, 
                generation_config=genai.types.GenerationConfig(
                    temperature=0.1,
                    max_output_tokens=700,
                )
            )
            resposta = response.text
            if not resposta:
                 resposta = "A IA não conseguiu gerar uma resposta para esta pergunta."

        except Exception as e:
            resposta = f"Erro ao gerar resposta da IA: {e}"
            print(resposta)
            flash(resposta, "danger")

    return render_template("cryptoia.html", form=form, resposta=resposta)