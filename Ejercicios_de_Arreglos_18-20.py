# Ejercicio 18 Sea un vector “Calificaciones” de 100 componentes.
class Vector_Calificacion():
    def __init__(self):
        pass

    def Calificacion(self):
        notas = []
        for i in range(100):
            califi = int( input( "Ingrese la calificacion {}: ".format(i)))
            notas.append(califi)
        print("Las calificaciones son: {}".format(notas))

cl= Vector_Calificacion()
cl.Calificacion()


# Ejercicio 19 leer un vector de 20 números enteros.
class Vector:
    def __init__(self):
        B= []
        A= []
        for i in range(20):
            Num=int(input("ingrese un numero: "))
            if Num >= 0:
                B.append(Num)
            else:
                A.append(Num)
        print("El numero positivo es",B)
        print("El numero negativo es",A)
Vec= Vector()


# Ejercicio 20 Se tiene información sobre las calificaciones de 6 exámenes de un grupo de 30 alumnos.
class cal_Examen:
    def __init__(self):
        notas_list=[]
        nom_list=[]
        alum=30
        casilla_notas=6
        prom_exa=[]

        for i in range (1,30):
            alumnos=input("Ingrese el nombre del Estudiante: ")
            nom_list.append(alumnos)
            for cal in range(1,7):
                notas=round(float(input("Ingrese las notas: ")),2)
                if cal ==1:
                    notas_list.append([notas])
                else:
                    notas_list[i-1].append(notas)

        """Calculo del promedio de calificaciones de cada exámen"""

        ex=1
        for calex in range(6):
            suma=0
            for cal in notas_list:
                suma+=cal[calex]
                promedio=round((suma/alum),2)
            prom_exa.append(promedio)
            print("El promedio general del examen {} es:{}".format(ex,promedio))
            ex+=1
        print(prom_exa)

        """cálculo del promedio de cada alumno"""

        for numero, i in enumerate(nom_list):
            suma=sum(notas_list[numero])
            prome=round((suma/casilla_notas),2)
            print("El promedio del Alumno {} es:{}".format(i,prome))

        """cálculo del tipo de examen que tuvo el mayor promedio de calificación"""

        mayor_exa=prom_exa.index(max(prom_exa))
        prom_mayor=max(prom_exa)
        print("El examen {} con el mejor promedio {} ".format(mayor_exa+1,prom_mayor))

final= cal_Examen()
