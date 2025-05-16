from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length 

class FormularioUsuario(FlaskForm):
    usuario = StringField('Usuário:', [validators.DataRequired(), validators.Length(min=1, max=20)])
    email = StringField('Email:', [validators.DataRequired(), validators.Length(min=1, max=100)])
    senha = PasswordField('Senha:', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Entrar')

class PerguntaForm(FlaskForm):
    pergunta = TextAreaField('Digite sua pergunta:', validators=[DataRequired()])
    enviar = SubmitField('Enviar')
