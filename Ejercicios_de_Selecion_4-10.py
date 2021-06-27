# ejercicio 4 calificación de un alumno en un examen.
class Calificaciones:
    def __ini__(self):
        pass

    def Cali(self):
        Cal= float(input("Ingrese la calificacion: "))
        if Cal >= 7:
            print("felicidades usted ha Aprobado: {}".format(Cal))

Cal1= Calificaciones()
Cal1.Cali()


# ejercicio 5 calificacion de un alumno y mostrar si Aprobo o Reprobado
class Calificaciones:
    def __ini__(self):
        pass

    def Cali(self):
        Cal= float(input("Ingrese la calificacion: "))
        if Cal >= 7:
            print("felicidades usted ha Aprobado: {}".format(Cal))
        else:
            print("Usted esta Reprobado")

Cal1= Calificaciones()
Cal1.Cali()


# Ejercicio 6 Aumento de sueldo 
class Sueldo_Aumento:
    def __init__(self):
        pass

    def Aumento(self):
        sueldo= float(input("Ingrese el sueldo del Empleado: "))
        if sueldo < 600:
            Nsueldo= sueldo+sueldo *0.10
            print("El sueldo mas Aumento: ",Nsueldo)
        else:
            Nsueldo= sueldo
            print("usted no est acto para recivir el Aumento:",sueldo)

Suel1= Sueldo_Aumento()
Suel1.Aumento()


# Ejercicio 7 horas extras
class ejercicio7:
    def __init__(self):
        pass

    def Horas_ext(self):
        ht= int(input("Ingrese el total de las horas trabajadas: "))
        ph= float(input("Ingrese el valor por horas trabajadas: "))
        if ht > 40:
            he= ht- 40
            if he > 8:
                het= he-8
                phe= ph * 2 * 8 + ph * 3 * het
            else:
                phe= ph * 2 * he
            pt= ph * 40 + phe
        else:
            pt= ph * ht
        print("El pago total de horas trabajadas es:", pt)

pago= ejercicio7()
pago.Horas_ext()


# Ejercicio 8 determinar el número mayor de los tres
class ejercicio8:
    def __init__(self):
        pass

    def Num_Mayor(self):
        num1= int(input("Ingrese su primer numero: "))
        num2= int(input("Ingrese su segundo numero: "))
        num3= int(input("Ingrese su tercer numero: "))
        if (num1 > num2) and (num1 > num3):
            NM= num1
            print("El numero mayor: {}".format(NM))
        else:
            if (num2 > num3):
                NM= num2
                print("El numero mayor: {}".format(NM))
            else:
                NM= num3
                print("El numero mayor: {}".format(NM))

NumMayor= ejercicio8()
NumMayor.Num_Mayor()


# Ejercicio 9 operaciones 
class ejercicio9:
    def __init__(self):
        self.opcion=int(input("Ingrese un numero del 1 al 3: "))
        self.num=int(input("Ingrese un numero: "))

    def opci(self):
        if self.opcion==1:
            mul=100*self.num
            print("El resultado de la operacion es: ",mul)
        elif self.opcion==2:
            pot=100**self.num
            print("El resultado de la operacion es: ",pot)
        elif self.opcion==3:
            div=100/self.num
            print("El resultado de la operacion es: ",div)

fun= ejercicio9()
fun.opci()


# Ejercicio 10 expresiones logicas 2 examenes a los aspirantes
class Aspirantes:
    def __init__(self):
        self.C1= int(input("Ingrese la primera nota: "))
        self.C2= int(input("Ingrese su segunda nota: "))
    def Notas(self):
        if self.C1 >=80 and self.C2>=80:
            print("La calificacion C1: {}, la calificación C2:{}, Usted ha sido ACEPTADO" .format(self.C1,self.C2))
        else:
            print("La calificacion C1: {} ,la calificación C2: {}, Usted ha sido RECHAZADO" .format(self.C1,self.C2))

Cal1= Aspirantes()
Cal1.Notas()

