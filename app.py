from flask import Flask, render_template
from flask import request
#para el manejo de cookies
from flask import make_response
#manejo de mensajes flask
from flask import flash
from flask_wtf import CSRFProtect

import forms
app = Flask(__name__)
app.config['SECRET_KEY']="esta es tu clave encriptada"
csrf=CSRFProtect()


@app.route('/Alumnos', methods=['GET', 'POST'])
def alumnos():
    reg_alumnos = forms.UserForm(request.form)
    mat = ""
    nom = ""
    if request.method == 'POST' and reg_alumnos.validate():
        mat = reg_alumnos.matricula.data
        nom = reg_alumnos.nombre.data
        # print(reg_alumnos.matricula.data)
        # print(reg_alumnos.nombre.data)
    return render_template('Alumnos.html', form=reg_alumnos, mat=mat, nom=nom)


@app.route('/CajasDinamicas', methods=['GET', 'POST'])
def cajasDinamicas():
    lista_num = forms.lista(request.form)
    num=0
    if request.method == 'POST':
        num = lista_num.numero.data
       
    return render_template('cajas.html', form=lista_num, num=num)  

@app.route('/Calcular', methods=['GET', 'POST'])
def calcular():
    if request.method == 'POST':
        numberList = request.form.getlist("txtNumeroL")
        number=list(map(int,numberList))
        may=max(number)
        mini=min(number)
       
        suma=0
    for valor in numberList:
        suma = suma + int(valor)
        cant = len(numberList)
        pro = suma / cant
        resultadoNumR=[]
    for valor1 in number:
        repeticion=number.count(valor1)
        resultadoNumR.append("{} aparece {} veces".format(valor1,repeticion))

    return render_template('cajasDinamicasResult.html',may=may,mini=mini,pro=pro,res=resultadoNumR)  

##############USO DE COOKIE ##############   
#definir decorador
@app.route("/cookie", methods=["GET","POST"])
def cookie():
    reg_user=forms.LoginForm(request.form,) #instanciar de la clase forlmulario 
    response= make_response(render_template('cookie.html',form=reg_user))
    if request.method=='POST' and reg_user.validate():
        usu=reg_user.username.data
        pasw = reg_user.password.data
        datos  = usu+"@"+pasw
        #Crear la cookie
        response.set_cookie('datos_user',datos)
      #  print( usu +" "+pasw)
        #crear mensaje de flask
        succes_message='Bienvenido {}'.format(usu)
        response.set_cookie('datos_user',datos)
        flash(succes_message)
    response= make_response(render_template('cookie.html',form=reg_user))
    return response 


@app.route("/traductor",methods=['GET','POST'])
def traductor():
    palabra={}
    with open('traductor.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                color, translation = line.split('=')
                palabra[color] = translation
    translation = ""
    if request.method == 'POST':
        if 'txtcolorEs' in request.form and 'txtcolorIn' in request.form:
            spanish_color = request.form['txtcolorEs']
            english_color = request.form['txtcolorIn']
            palabra[spanish_color] = english_color
            with open('traductor.txt', 'a') as f:
                f.write(f"{spanish_color.lower()}={english_color.lower()}\n")
                f.write(f"{english_color.lower()}={spanish_color.lower()}\n")
            flash("Palabra añadida con éxito.")
        elif 'color' in request.form and 'rbgidioma' in request.form:
            color = request.form['color'].lower()
            language = request.form['rbgidioma']
            if color in palabra:
                if language == 'rbingles':
                    translation = palabra[color]
                if language == 'rbespaniol':
                    translation = palabra[color]
            else:
                flash(f"la palabra {color} no está registrado.")
    return render_template('traductor.html', translation=translation, form=request)



if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)