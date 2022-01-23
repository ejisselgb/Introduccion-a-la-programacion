def cast_nota(valor):
    return float(valor)

def calcular_iva(valor):
    print("valor ", valor)
    iva = valor * 0.19
    print("iva ", iva)
    total = valor + iva
    print("total ", total)
    return total

print("Ingresa el valor de los productos comprados")


producto1 = input("Digite el valor del producto 1 ")
producto2 = input("Digite el valor del producto 2 ")
producto3 = input("Digite el valor del producto 3 ")

total_p1 = calcular_iva(cast_nota(producto1))
total_p2 = calcular_iva(cast_nota(producto2))
total_p3 = calcular_iva(cast_nota(producto3))

total_productos = total_p1 + total_p2 + total_p3

print("El precio de los tres artículos incluyendo iva es: ", total_productos)


