Algoritmo Calculo_Promedio
	Escribir "Ingresa en el sistema las notas del estudiante"
	quices = 0
	intentosQuices = 1
	parcial = 0
	intentosParciales = 1
	trabajos = 0
	intentosTrabajos = 1

	Repetir
		Escribir "Ingresa la  nota " intentosQuices " para quices"
		Leer nota
		
		quices = quices + nota
		intentosQuices = intentosQuices + 1
	Hasta Que intentosQuices >= 4
	
	//3.5 + 2.4 + 3.7
	promedio_quices = (quices / 3) * 0.2
	Escribir "Nota total para quices " promedio_quices
	
	//4.0 + 2.6 + 3.0
	Repetir
		Escribir "Ingresa la  nota " intentosParciales " para parciales"
		Leer nota
		
		parcial = parcial + nota
		intentosParciales = intentosParciales + 1
	Hasta Que intentosParciales >= 4
	
	promedio_parciales = (parcial/3) * 0.5
	Escribir "Nota total para parciales " promedio_parciales
	
	Repetir
		Escribir "Ingresa la  nota " intentosTrabajos " para trabajos"
		Leer nota
		
		trabajos = trabajos + nota
		intentosTrabajos = intentosTrabajos + 1
	Hasta Que intentosTrabajos >= 3
	
	//3.7 + 4.8
	promedio_trabajos = (trabajos/2) * 0.3
	Escribir "Nota total para trabajos " promedio_trabajos
	
	total_nota_curso = promedio_quices + promedio_parciales + promedio_trabajos
	Escribir "Nota total del curso " total_nota_curso
FinAlgoritmo
