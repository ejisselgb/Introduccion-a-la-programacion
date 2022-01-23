from clases.Personaje import * 
import random
import sys

#Creación de personajes
#Nombre, ataque, vida, vive
cientifico = Personaje("Cientifico", 20, 100)
biologo = Personaje("Biologo", 30, 100)
quimico = Personaje("Quimico", 15, 100)

equipo = {"cientifico": cientifico, "biologo": biologo, "quimico": quimico}

def luchar(nombrePersonaje, personaje):
    lucha = True
    turno = random.randint(0,1) #0 para cientifico, 1 para bacteria, 2 para virus
    ataqueEnemigo = random.randint(10,50)
    nombreEnemigo = ""
    if(ataqueEnemigo >= 10 and ataqueEnemigo <= 30):
        nombreEnemigo = "Bacteria"
    else:
        nombreEnemigo = "Virus"
    enemigo = Personaje(nombreEnemigo, ataqueEnemigo, 100)
    print("\n--------------------------------\n")
    enemigo.getCaracteristicas()
    print("\n--------------------------------\n")
    while(lucha):
        if(turno == 0):
            ataque = personaje.getAtaque()
            enemigo.recibirAtaque(ataque)
            turno = 1
        else:
            ataque = enemigo.getAtaque()
            personaje.recibirAtaque(ataque)
            turno = 0
        
        if(personaje.vida <= 0 or enemigo.vida <= 0):
            lucha = False

    if(personaje.vida > 0):
        print("\n--------------------------------\n")
        print("Derrotaste a las bacterias y virus, ¡Lo lograste!")
        print("Vida del "+nombrePersonaje+": "+str(personaje.vida))
        print("Vida del microorganismo: "+str(enemigo.vida))
        print("\n--------------------------------\n")
    else:
        print("\n--------------------------------\n")
        print("Las bacterias y virus seguirán dominando al mundo, has perdido")
        print("Vida del "+nombrePersonaje+": "+str(personaje.vida))
        print("Vida del microorganismo: "+str(enemigo.vida))
        print("\n--------------------------------\n")


inicio = True
while(inicio):
    print("\n################################\n")
    print("CAMPO DE BATALLA")
    print("\n################################\n")
    opcion = input("\n-----\nEscribe la opción que deseas seleccionar: \n1.Atacar\n2.Salir\n\n-----\n")
    if opcion == "1":
        personaje = input("\n-----\nEscribe el nombre del personaje que utilizarás para atacar: \nC.científico\nB.biólogo\nQ.químico\n-----\n")
        key = ""

        if(personaje == "C"):
            key="cientifico"
        elif(personaje == "B"):
            key="biologo"
        elif(personaje ==  "Q"):
            key="quimico"
        if key in equipo:
            luchar(key,equipo[key])
        else:
            print("\n-----\nEl personaje seleccionado no es válido\n-----\n")
    else:
        sys.exit()

