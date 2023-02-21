from wtforms import Form 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, IntegerField
from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField

#crear la clase 
class UserForm(Form):
    matricula=StringField('Matricula')
    nombre=StringField('Nombre')
    apaterno=StringField('ApPaterno')
    amaterno=StringField('ApMaterno')
    email=EmailField('Correo')

class lista(Form):
    numero=IntegerField('Numero')
