n = int(input("Ingrese el número que desea validar "))
m = int(input("Ingrese el numero del divisor "))

calculo_mod = n % m

if calculo_mod == 0:
    print("El número es múltiplo de: " + str(m))
else:
    print("El número NO es múltiplo de: " + str(m))
