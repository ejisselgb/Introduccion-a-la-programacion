Funcion calculo <- cal_fibonacci ( num )
	Si num < 2 Entonces
		calculo<-num
	SiNo
		calculo<-cal_fibonacci(num-1)+cal_fibonacci(num-2)
	Fin Si
Fin Funcion


Algoritmo Fibonacci
	Escribir "Tama�o de la serie fibonacci"
	Leer size
	Para c<-0 Hasta size Hacer
		Escribir cal_fibonacci(c)
	Fin Para
FinAlgoritmo




