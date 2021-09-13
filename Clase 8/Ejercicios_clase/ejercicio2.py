ataque = 10
tipo_ataque = "completo"

def calcular_puntos(ataque, tipo_ataque):
    puntos = 0
    while ataque > 10:
        if(tipo_ataque == "completo"):
            puntos = puntos + 5
        elif(tipo_ataque == "medio"):
            puntos = puntos + 3
        else:
            puntos = puntos + 0 
        ataque = ataque - 1
    return puntos

puntuacion = calcular_puntos(ataque, tipo_ataque)
print("Los puntos obtenidos son: " + str(puntuacion))