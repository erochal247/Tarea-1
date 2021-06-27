#ejercicio 1 Encontrar la superficie de un círculo para un radio cualquiera.

class Superficie:
    def __init__(self):
        pass

    def su_circulo(self):
        rad= float(input("Ingrese el radidio del circulo: "))
        sup= 3.1416*(rad**2)
        print("La superficie del círculo es {}" .format(sup))

obje=Superficie()
obje.su_circulo()
