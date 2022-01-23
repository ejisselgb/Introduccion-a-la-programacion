Algoritmo Validar_contrasena
	Repetir
		Escribir "Escribe una contraseña"
		Leer contrasena
		Si Longitud(contrasena) = 8 Entonces
			Si contrasena = "miclave1" Entonces
				Escribir "La contraseña es correcta"
			SiNo
				Escribir "La contraseña no coincide con la esperada"
			Fin Si
		SiNo
			Escribir "La contraseña no tiene el tamaño esperado"
		Fin Si	
	Hasta Que (Longitud(contrasena) = 8)  & (contrasena = "miclave1")
FinAlgoritmo
