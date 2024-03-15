import random

def juego_de_adivinanza():
    numero_secreto = random.randint(1, 15)
    intentos = 0

    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 15.")

    while True:
        guess = int(input("¿Cuál crees que es el número?: "))

        intentos += 1

        if guess < numero_secreto:
            print("Demasiado bajo. ¡Intenta con un número más alto!")
        elif guess > numero_secreto:
            print("Demasiado alto. ¡Intenta con un número más bajo!")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            

# Ejecutar el juego
juego_de_adivinanza()


