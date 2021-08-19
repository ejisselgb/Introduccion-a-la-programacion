from typing import cast


def cast_nota(nota):
    return float(nota)

print("Ingrese las notas obtenidas durante del semestre")

nota1 = input("Digite la nota 1 ")
nota2 = input("Digite la nota 2  ")
nota3 = input("Digite la nota 3  ")
nota4 = input("Digite la nota 4  ")
nota5 = input("Digite la nota 5  ")

suma_notas = cast_nota(nota1) + cast_nota(nota2) + cast_nota(nota3) + cast_nota(nota4) + cast_nota(nota5)
total_nota = suma_notas / 5

print("La suma de las notas es: ", total_nota)





