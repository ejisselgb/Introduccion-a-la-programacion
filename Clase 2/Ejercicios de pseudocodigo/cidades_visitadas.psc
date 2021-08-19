Algoritmo cidades_visitadas
	Definir ciudades Como Entero
	Escribir "Lista de las ciudades visitdas"
	Leer ciudades 
	
	Para item<-1 Hasta ciudades  Hacer
		Si (item%2) = 0 Entonces
			Escribir "Visite esta ciudad"
		SiNo
			Escribir "No visite esta ciudad"
		Fin Si
	Fin Para
	
FinAlgoritmo
