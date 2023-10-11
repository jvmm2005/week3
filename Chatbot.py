#Examen de matemáticas
nota = 0
respuesta1 = "e"
respuesta2 = "3x3"
respuesta3 = "si"
respuesta4 = 1
respuesta5 = "no"
print ("""Hola! bienvenido a tu peor pesadilla, osea... bienvenido a este examen de matemáticas sorpresa \n Antes de nada voy a hacerte unapequeña guía, yo no entiendo: 
MAYÚSCULAS, acentos/tildes, los decimales me los pones con puntos, las comas son para niños, y solo acepto respuestas, ni sugerencias, ni dudas. 
\n Buena suerte""")
pregunta1 = (input("Esta es fácil, 1º: Cual es tu nombre:"))
print ("""Enhorabuena, has suspendido la pregunta nombre, no te lo enseñaron en la escuela?, el nombre siempre en mayúsculas!!! \n bromas a parte, comenzemos \n Cuál de estos números es irracional: e, 2, raíz de un número negativo. (escribe el número tal cual está ahora)""")
R1 = str(input("Escribe la respuesta aquí:"))
if (R1 == respuesta1):
    print ("Correcto")
    nota = nota + 1
else:
    print ("Fallaste")
print ("Segunda pregunta: \n Cual de las siguientes es una matriz cuadrada: 3x3 o 4x2.")
R2 = str(input("Responde aquí:"))
if (R2 == respuesta2):
    print ("correcto")
    nota = nota + 1
else:
    print ("fallaste")
print ("Tercera pregunta: (vale por 3) \n ¿El rango de una matriz 3x4 depende de la dependencia lineal de los vectores que forman sus filas?")
R3 = str(input("si o no:"))
if (R3 == respuesta3):
    print ("correcto")
    nota = nota +3
print ("Cuarta pregunta: Cual es el rango de la matriz formada por dos planos que se contienen")
R4 = float(input("Escribe aquí tu respuesta:"))
if (R4 == respuesta4):
    print ("correcto")
    nota = nota + 1
else:
    print ("fallaste")
print ("Última pregunta: Vale por 2. ¿Es el número +-3 idéntico a la raíz del número nueve?")
R5 = str(input("Escribe tu respuesta aquí:"))
if (R5 == respuesta5):
    print ("correcto")
    nota = nota + 2
else:
    print ("fallaste")
if (nota >= 5):
    print ("Enhorabuena, has aprobado (haciendo trampas seguro)")
else:
    print ("Has suspendido, a nadie le sorprende")