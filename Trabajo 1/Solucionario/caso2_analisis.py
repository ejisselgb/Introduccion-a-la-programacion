#Solucion sin funciones.
import math

latitud = 6.252574
longitud = -75.565096

grados_dd, grados = math.modf(latitud)
grados = str(int(grados))
minutos = grados_dd * 60
minutos_dd, minuto = math.modf(minutos)
segundos = minutos_dd * 60
segundos = round(float(segundos),1)


if(segundos < 10):
    segundos = "0"+str(segundos)


print("La latitud en coordenadas decimales es: " + grados + "°" + str(int(minuto)) + "'" + str(segundos) + '"' + "N")


longitud = abs(longitud) #Para pasar el número de negativo a positivo y realizar las operaciones sin problemas - valor absoluto
grados_dd_lon, grados_lon = math.modf(longitud)
grados_lon = grados_lon
grados_lon = str(int(grados_lon))
minutos_lon = grados_dd_lon * 60
minutos_dd_lon, minuto_lon = math.modf(minutos_lon)
minuto_lon = minuto_lon
segundos_lon = minutos_dd_lon * 60
segundos_lon = round(float(segundos_lon),1)
segundos_lon = segundos_lon

print("La latitud en coordenadas decimales es: " + grados_lon + "°" + str(int(minuto_lon)) + "'" + str(segundos_lon) + '"' + "W")

#La latitud en coordenadas decimales es: 6°15'09.3"N
#La latitud en coordenadas decimales es: 75°33'54.3"W