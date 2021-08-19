print("Digite dos número para realizar la operación de suma, resta, multiplicación y división")
numero1 = input("Digite el número 1 ")
numero2 = input("Digite el número 2 ")


numero1_cast = int(numero1)
numero2_cast = int(numero2)

suma = numero1_cast + numero2_cast
resta = numero1_cast - numero2_cast
multi = numero1_cast * numero2_cast
division = numero1_cast / numero2_cast

print("El resultado de la suma es: ", suma)
print("El resultado de la resta es: ", resta)
print("El resultado de la multiplicación es: ", multi)
print("El resultado de la división es: ", division)
