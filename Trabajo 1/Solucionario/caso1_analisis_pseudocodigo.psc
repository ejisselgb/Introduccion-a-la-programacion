Algoritmo generacion_bacteriana
	Escribir "C�lculo del tiempo de generaci�n bacteriana"
	Escribir "�Desea empezar?, ingrese SI o NO, en mayusculas y sin espacios:"
	Leer empezar
	
	
	Si (empezar <> "SI") & (empezar <> "NO")  Entonces
		Escribir "El comando ingresado no es v�lido "
	SiNo
		Mientras empezar == "SI" 
			Escribir "Ingresa el nombre de la bacteria a analizar:"
			Leer nombre_bacteria
			Escribir "Ingresa el n�mero de bacterias inicial en el tiempo 0:" 
			Leer x
			Escribir "Ingresa el n�mero de bacterias al tiempo de finalizaci�n :"
			Leer y_t
			Escribir "Ingresa el tiempo de crecimiento:"
			Leer t
			
			n = 3.3 * (ln(y_t/x) / ln(10))
			t = t * 60
			g = t/n
			
			Escribir "Tiempo de generaciones para la bacteria " nombre_bacteria " es:" g
			Escribir "N�mero de generaciones para la bacteria " nombre_bacteria " es: " n
			
			Escribir "Desea analizar una nueva bacteria"
			Leer empezar
		Fin Mientras
	Fin Si
	
	Escribir "Cerrar programa"
	
FinAlgoritmo
