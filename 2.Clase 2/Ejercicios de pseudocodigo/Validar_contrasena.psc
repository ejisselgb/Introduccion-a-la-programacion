Algoritmo Validar_contrasena
	Repetir
		Escribir "Escribe una contrase�a"
		Leer contrasena
		Si Longitud(contrasena) = 8 Entonces
			Si contrasena = "miclave1" Entonces
				Escribir "La contrase�a es correcta"
			SiNo
				Escribir "La contrase�a no coincide con la esperada"
			Fin Si
		SiNo
			Escribir "La contrase�a no tiene el tama�o esperado"
		Fin Si	
	Hasta Que (Longitud(contrasena) = 8)  & (contrasena = "miclave1")
FinAlgoritmo
