Algoritmo calculo_modulo
    Escribir "Capture 3 n�meros y valide si estos son un n�mero par"
	intentos = 0
	
	Repetir
		Leer num
		operacion = num % 2
		Si operacion == 0 Entonces
			Escribir  "El n�mero " num " es PAR"
		SiNo
			Escribir  "El n�mero " num " es IMPAR"
		Fin Si
		intentos = intentos + 1
	Hasta Que intentos >= 3
FinAlgoritmo
