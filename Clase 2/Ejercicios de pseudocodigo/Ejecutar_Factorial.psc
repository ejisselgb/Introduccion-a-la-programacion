Funcion facto<-factorial(number)
	si(number=1) Entonces
		facto<-1
	SiNo
		facto<-number*factorial(number-1)
	FinSi
FinFuncion

Algoritmo Ejecutar_Factorial
	resultado_factorial<-factorial(3)
	Escribir resultado_factorial
FinAlgoritmo


