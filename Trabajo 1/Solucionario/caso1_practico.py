#La solucion se plantea sin hacer uso de funciones, ya que hasta este taller ese tema no se habia visto en clase

import math

print("Cálculo del tiempo de generación bacteriana")
empezar = input("¿Desea empezar?, ingrese SI o NO, en mayusculas y sin espacios: ")

if(empezar != "SI" and empezar != "NO"):
    print("El comando ingresado no es válido")
else:
    while(empezar == "SI"):
        nombre = input("Ingresa el nombre de la bacteria a analizar: ")
        x = int(input("Ingresa el número de bacterias inicial en el tiempo 0: "))
        y = int(input("Ingresa el número de bacterias al tiempo de finalización : "))
        t = int(input("Ingresa el tiempo de crecimiento: "))

        n = 3.3*math.log10( y/x ) #Numero de generaciones
        t_m = t * 60
        G = t_m/n #Tiempo de generaciones

        print("Tiempo de generaciones para la bacteria " + nombre + " ", round(G,2))
        print("Número de generaciones para la bacteria " + nombre + " ", n)

        print("Desea analizar una nueva bacteria")
        empezar = input("Ingrese SI o NO para continuar: ")

print("Cerrar programa")

