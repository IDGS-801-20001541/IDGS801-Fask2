#Usar archvos de texto #
#cear un flujo de variable 
#'r' leer el archivo 'w' escribir 
file=open('alumnos2.txt','a')
file.write('\n'+'¡Hola Mundo!! ')
file.write('\n'+'¡Hola Mundo 2!! ')

#leer el archivo  readlines*manda todo el contenidodel archivo 
#nombre=file.readline() # solo el primer dato del archivo
#print(nombre)

#cerrarelflujo
file.close()
"""for item in nombre: 
    item(item,end='')"""
