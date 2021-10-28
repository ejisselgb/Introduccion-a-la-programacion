candidatos = ["Pepe", "Violeta", "Mayo", "Flor"]
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
conteo_votos = []

personas_votos = 10

while(personas_votos > 0):
    votante = input(
        "Elige la persona por la que deseas votar: "+str(candidatos)+": ")
    exists = votante in candidatos

    if(exists):
        if(votante == "Pepe"):
            candidato1 = candidato1 + 1
        elif(votante == "Violeta"):
            candidato2 = candidato2 + 1
        elif(votante == "Mayo"):
            candidato3 = candidato3 + 1
        else:
            candidato4 = candidato4 + 1
        personas_votos = personas_votos - 1
    else:
        print("El candidato ingresado no existe")


cantidad_votos = {"Pepe": candidato1, "Violeta": candidato2,
                  "Mayo": candidato3, "Flor": candidato4}

#Se realiza de esta manera para tener en cuenta los conceptos vistos en clase y usar funcionalidades que están bajo nuestro dominio

#Se captura el valor de la llave uno y así tener una referencia                
numero = cantidad_votos["Pepe"]
#Se crea una variable que va a tener el nombre del ganador
nombre_ganador = ""
#Se recorre con un for el diccionario que contiene la cantidad de votos y se valida si el valor tomado y almacenado en i, es menor que el numero inicial
for i in cantidad_votos:
    if(cantidad_votos[i] > numero):
        numero = cantidad_votos[i]
        nombre_ganador = i

print("El ganador es: ", nombre_ganador, " con ", numero, " votos")

#Otra manera es, crear una lista con los valores numericos del diccionario y usar la funcion max() que permite obtener el valor maximo de una lista
lista_votos = []
nombre_candidato = ""
for i in cantidad_votos:
    lista_votos.append(cantidad_votos[i])

cantidad_ganador = max(lista_votos)

for i in cantidad_votos:
    if cantidad_votos[i] == cantidad_ganador:
        nombre_candidato = i

print("Usando otra forma para mostrar el ganador")
print("Nombre ganador: ", nombre_candidato, " \nCantidad de votos: ", cantidad_ganador) #El \n se utiliza para el salto de linea

