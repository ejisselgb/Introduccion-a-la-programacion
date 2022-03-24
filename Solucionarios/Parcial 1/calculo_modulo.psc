Algoritmo calculo_modulo
    Escribir "Capture 3 números y valide si estos son un número par"
	intentos = 0
	
	Repetir
		Leer num
		operacion = num % 2
		Si operacion == 0 Entonces
			Escribir  "El número " num " es PAR"
		SiNo
			Escribir  "El número " num " es IMPAR"
		Fin Si
		intentos = intentos + 1
	Hasta Que intentos >= 3
FinAlgoritmo
