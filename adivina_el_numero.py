from random import *

# entrada
numero_ingresado = int(input("Ingrese un número del 1 al 15: "))
# proceso

numero_generado = randint(1, 15)

if numero_ingresado == numero_generado:
    print("Felicidades, adivinaste el número")
elif numero_ingresado < numero_generado:
    print("El número a adivinar es mayor a", str(numero_ingresado), "era el", str(numero_generado))
else:
    print("El número a adivinar es menor a", str(numero_ingresado), "era el", str(numero_generado))

