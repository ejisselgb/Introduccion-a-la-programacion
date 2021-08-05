Algoritmo Validar_Numero
	Repetir
		Escribir "Escribir numero"
		Leer number
		Si number%2 <> 0 Entonces
			Escribir "Ese número no es divisible por 2"
		SiNo
			Escribir "Número correcto"
		FinSi
	Hasta Que number%2 = 0
	Escribir "Fin del algoritmo"
FinAlgoritmo

