import os
from flask import Flask
import google.generativeai as genai
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)

# Certifique-se que database/config.py existe e configura SQLALCHEMY_DATABASE_URI etc.
app.config.from_pyfile('database/config.py')
app.config['SECRET_KEY'] = SECRET_KEY

if not GEMINI_API_KEY:
    print("ERRO: A chave API do Gemini (GEMINI_API_KEY) não foi carregada das variáveis de ambiente.")
    print("Verifique se o arquivo .env existe e contém a chave.")
else:
    genai.configure(api_key=GEMINI_API_KEY)

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)


from views import *

if __name__ == '__main__':
    app.run(debug=True)