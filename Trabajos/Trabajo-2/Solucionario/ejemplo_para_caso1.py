texto1 = input("INGRESE EL PRIMER TEXTO 1 ")
texto2 = input("INGRESE EL PRIMER TEXTO 2 ")
lista = []
nueva_lista = []


def validar_tamano(texto):
    if(len(texto) >= 5 and len(texto) <= 10):
        lista.append(texto)
    else:
        print("El texto " + texto +
              " ingresado no cumple con las características, ingrese uno nuevamente")
        nuevo_texto = input("INGRESE NUEVAMENTE UN TEXTO ")
        validar_tamano(nuevo_texto)


validar_tamano(texto1)
validar_tamano(texto2)

print(lista)


for texto in lista:  # Este primer for, se encarga de recorrer a la lista para obtener la cadena de texto por cada
    # Hacer que esto sea una función ###########################33
    reconstruir_cadena = ""
    for letra in texto:  # Este for se encarga de recorrer letra por letra para que esta pueda ser validada
        if(letra == "A" or letra == "B" or letra == "C"):
            reconstruir_cadena = reconstruir_cadena + letra
        else:
            reconstruir_cadena = ""
            break  # Rompe el segundo for que se encarga de obtener letra por letra, pasa al primer for para capturar la palabra que sigue
    ###### Fin funcion ##################################################################
    if reconstruir_cadena:
        reconstruir_cadena = reconstruir_cadena.replace("A", "D")
        nueva_lista.append(reconstruir_cadena)
    else:
        print("La cadena de texto " + texto +
              " no cumplia con la condicion de tener solo las letras A, B, C. Por eso no se pueden agregar")

print("\n LISTA FINAL Y VALIDA ", nueva_lista)
