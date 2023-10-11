masa = float(input("Indique la masa de su planeta en kilogramos:"))         #Creación de variables
radio = float(input("Indique el radio del planeta:"))
Constantedelagravedad = 6.67E-11
fuerzaG = ((Constantedelagravedad*masa)/radio**2)                           #Creación de la gravedad del planeta
print ("La gravedad de su planeta es de:", fuerzaG, "m/s.s")
Tiempo = float(input("Indique el tiempo transcurrido desde el lanzamiento del objeto:"))
altura = float(input("Indique la altura desde que lanza el objeto:"))
posición = ((fuerzaG*Tiempo**2)/2)                                          #Cálculo de la posición del objeto
alturafinal = (altura - posición)
if (posición < altura):
    print ("El cuerpo ha recorrido", posición, "metros, y ahora está a:", alturafinal , "metros de la superficie.")
else:
    print ("El cuerpo de ha estampado contra tu planeta, prueba a introducir una menor masa para disminnuir la aceleración, a introducir menos tiempo transcurrido o a lanzar el objeto desde una altura mayor")