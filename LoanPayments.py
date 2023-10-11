#Estos son los tipos de interes que varían cada 6 meses
I1 = 8.04
I2 = 9.38
I3 = 6.74
I4 = 4.02
I5 = 12.35
I6 = 10.91
#Aquí obtenemos los valores con los que nos moveremos dependiendo de la vida del préstamo
MesesPrestar = float(input("Indique la vida del préstamo:"))
Préstamo1 = float(input("Seleccione la cantidad a prestar:"))
#Estas son las mensualidades con su respectiva cantidad de préstamo restante,debido al cambio del tipo de interes bianual
Mensualidad1 = ((Préstamo1+(Préstamo1*(I1/100)))/MesesPrestar)
Préstamo2 = (Préstamo1)-(Mensualidad1)
Mensualidad2 = ((Préstamo2+(Préstamo2*(I2/100)))/(MesesPrestar-6))
Préstamo3 = (Préstamo2-(6*Mensualidad2))
Mensualidad3 = ((Préstamo3+(Préstamo3*(I3/100)))/(MesesPrestar-12))
Préstamo4 = (Préstamo3-(6*Mensualidad3))
Mensualidad4 = ((Préstamo4+(Préstamo4*(I4/100)))/(MesesPrestar-18))
Préstamo5 = (Préstamo4-(6*Mensualidad4))
Mensualidad5 = ((Préstamo5+(Préstamo5*(I5/100)))/(MesesPrestar-24))
Préstamo6 = (Préstamo5-(6*Mensualidad5))
Mensualidad6 = ((Préstamo6+(Préstamo6*(I6/100)))/(MesesPrestar-30))
#Esta parte indica y escribe la mensualidad correspondiente en función del dinero y meses restantes
if (MesesPrestar <= 6):
    print (Mensualidad1)
else:
    if (MesesPrestar <= 12):
        print ("Su mensualidad final a pagar es de" , (Mensualidad2))
    else:
        if (MesesPrestar <= 18):
            print ("Su mensualidad final a pagar es de" , (Mensualidad3))
        else:
            if (MesesPrestar <= 24):
                print ("Su mensualidad final a pagar es de" , (Mensualidad4))
            else:
                if (MesesPrestar <= 30):
                    print ("Su mensualidad final a pagar es de" , (Mensualidad5))
                else:
                    if (MesesPrestar > 30):
                        print ("Su mensualidad final a pagar es de" , (Mensualidad6))