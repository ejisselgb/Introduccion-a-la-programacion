def sumar(numero1, numero2):
    return numero1 + numero2
 
producto1  = float(input("Ingrese el precio de producto 1: "))
producto2 = float(input("Ingrese el precio de producto 2: "))
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))

def calculo_iva():
    return sumar(producto1, producto2)*0.19

def sumar_productos():
    return sumar(producto1, producto2)

def calculo_nota():
    return sumar(nota1, nota2)/2

print("Calculo iva de dos productos ", calculo_iva())
print("Suma de productos ", sumar_productos())

producto_iva = sumar_productos() + calculo_iva()

print("Productos + iva ", producto_iva)

print("Promedio de notas ", calculo_nota())


