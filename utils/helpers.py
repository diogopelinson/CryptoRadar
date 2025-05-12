from main import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField


class FormularioUsuario(FlaskForm):
    usuario = StringField('Usúario:', [validators.DataRequired(), validators.Length(min=1, max=20)])
    email = StringField('Email:', [validators.DataRequired(), validators.Length(min=1, max=100)])
    senha = PasswordField('Senha:', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Entrar')