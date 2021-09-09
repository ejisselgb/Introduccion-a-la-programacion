def factorial(number):
    if (number == 0): return 1
    return number * factorial (number-2)

permutaciones = 3**8
edges = 2**12
combinaciones = (factorial(8) * permutaciones * factorial(12) * edges) / (2*3*2)
print ("El número de combinaciones para el cubo de Rubik 3x3 es: ")
print(combinaciones)






