Algoritmo mi_algoritmo
	Escribir "Ingrese valor del producto"
	Leer prod
	calculo_iva = prod * 0.19
	valor_iva = prod + calculo_iva
	
	Si valor_iva >= 20000 Entonces
		valor_descuento = valor_iva - 3000
		Escribir "El producto APLICA descuento"
	SiNo
		valor_descuento= valor_iva
		Escribir  "El producto NO aplica descuento"
	Fin Si
	
	Escribir  "Valor real del producto: " valor_iva
	Escribir  "Valor total a pagar del producto: " valor_descuento
FinAlgoritmo

