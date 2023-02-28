#Usar archvos de texto #
#cear un flujo de variable 
#'r' leer el archivo 'w' escribir 
file=open('alumnos.txt','r')
#file.write('\n'+'¡Hola Mundo!! ')
#file.write('\n'+'¡Hola Mundo 2!! ')
contenido = file.read()
palabra = 'iana'
if palabra in contenido:
    print(palabra)
else:
    print('La palabra no está en el archivo')

#leer el archivo  readlines*manda todo el contenidodel archivo 
#nombre=file.readline() # solo el primer dato del archivo
#print(nombre)

#cerrarelflujo
file.close()
"""for item in nombre: 
    item(item,end='')"""
