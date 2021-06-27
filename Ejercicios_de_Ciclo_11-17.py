# Ejercicio 11 cuadrados de los primeros 100 enteros y escribir el resultado.
class cuadrado:
    def __init__(self):
        self.suma=0
    def numero(self):
        for i in range(0,100,1):
            self.suma+=i**2
            print("La suma de los cuadrados es: ",self.suma)

obj= cuadrado()
obj.numero()


# Ejercicio 12 escribir los números del 1 al 100
class Numeros:
    def __init__(self):
        self.i=1
    def secu(self):
        while self.i<=100:
            print(self.i)
            self.i=self.i+1

num= Numeros()
num.secu()


# Ejercicio 13 suma y producto de N números enteros
class Suma:
    def __init__(self):
        self.n="si"
        self.suma= 0
        self.prod= 1
    def sum(self):
        while self.n!="no":
            num=int(input("Ingrese numero: "))
            self.suma+=num
            self.prod=self.prod*num
            self.n=input("Desea continuar si/no: ")
            self.n=self.n.lower()
        print("El total de la suma es: {}, y el producto es: {}".format(self.suma,self.prod))
resul= Suma()
resul.sum()


# Ejercicio 14 suma y producto de N números enteros
class Suma_P:
    def __init__(self):
        print("El bucle terminara cuando se ingrese un numero menor que 1")
        self.suma= 0
        self.prod= 1
        self.num=int(input("Ingrese numero: "))
    def sum (self):
        while self.num != 0:
            self.suma+=self.num
            self.prod=self.prod*self.num
            self.num=int(input("Ingrese numero: "))
        print("El total de la suma es: {}, y el producto es: {}".format(self.suma,self.prod))

resul= Suma_P()
resul.sum()


# Ejercicio 15 Determinar si un número entero proporcionado por el usuario es primo.
class Primo:
    def __init__(self):
        self.primo= 0
        self.num=int(input("Ingrese numero: "))
        for i in range(1, self.num+1):
            if self.num % i == 0:
                self.primo+= 1

        if self.primo== 2:
            print("Numero",self.num, "es primo")
        else:
            print("Numero",self.num, "no es primo")
de= Primo()



# Ejercicio 16 calcular el resultado de la siguiente serie.
class Serie:
    def __init__(self):
        self.serie=0
        self.I= 1
        self.N= int(input("Ingrese numero: "))
        self.Band="True"
        while self.I <= self.N:
            if self.Band == "True":
                Ser=(self.serie + 1/self.I)
                self.Band="False"
            else:
                Ser=(self.serie - 1/self.I)
                self.Band="True"
            self.I +=1
            if self.I > self.N :
                break
        print("El resultado de la serie es: {}",Ser)
obje= Serie()


# Ejercicio 17 Calcular el factorial de N números enteros.
class Factorial:
    def __init__(self):
        pass
    def calculo (self):
        n=int(input("Ingrese un numero: "))
        for i in range(1, n+1):
            n=int(input("Ingrese un numero: "))
            fact= 1
            for j in range(1, n+1):
                fact=fact*j
            print("El factorial del número",n, "es", fact)
facto= Factorial()
facto.calculo()
