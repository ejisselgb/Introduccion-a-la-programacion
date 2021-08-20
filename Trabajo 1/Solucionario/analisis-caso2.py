def numberCombinatory():
    permutations = 3**8
    edges = 2**12
    combinations = (factorialNumber(8) * permutations * factorialNumber(12) * edges) / (2*3*2)
    print ("El número de combinaciones para el cubo de Rubik 3x3 es: ")
    print(combinations)
    
def factorialNumber(number):
    if (number == 0): return 1
    return number * factorialNumber (number-1)

numberCombinatory()






