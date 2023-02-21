from flask import Flask, render_template
from flask import request

import forms
app = Flask(__name__)


@app.route('/Alumnos', methods=['GET', 'POST'])
def alumnos():
    reg_alumnos = forms.UserForm(request.form)
    mat = ""
    nom = ""
    if request.method == 'POST':
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


if __name__ == "__main__":
    app.run(debug=True, port=3000)
