from wtforms import Form 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, IntegerField
from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField
from wtforms import validators


def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError('El campo esta vacio')
#crear la clase 
class UserForm(Form):
    matricula=StringField('Matricula',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='Se requiere una longitud minima de 4 o 5 caracteres ')
    ])
    nombre=StringField('Nombre',[
        validators.DataRequired(message='El campo es requerido')
    ])
    apaterno=StringField('ApPaterno',[mi_validacion])
    amaterno=StringField('ApMaterno')
    email=EmailField('Correo')

class LoginForm(Form):
    username= StringField('usuario',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='Se requiere una longitud minima de 4 o 5 caracteres ')
    ])
    password= StringField('password',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='Se requiere una longitud minima de 4 o 5 caracteres ')
    ])

class diccionario(Form):
    español= StringField('Español',[
        validators.DataRequired(message='El campo es requerido')
    ])
    ingles= StringField('Ingles',[
        validators.DataRequired(message='El campo es requerido')
    ])
   
   
class lista(Form):
    numero=IntegerField('Numero')
