#We are going to calculate the area of a equilateral triangle in 3 dimensions, asking for side lenght and altitude
side = float(input("please, give the size of the siza lenght:"))
def area(altitude, sidelenght):
    area = (((sidelenght*sidelenght/2)/2)*altitude)
    return area
altitudeimput = float(input("Altitude:"))
sidelenghtimput = float(input("Side lenght:"))
calculatedarea = area(altitudeimput,sidelenghtimput)
print(calculatedarea)