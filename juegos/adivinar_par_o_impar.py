import random 
def adivinar_par_o_impar():
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """

    numero = random.randint(1,10)
    adivinanza = input()
    resultado = input()

    if numero %2 == 0:
        resultado = "par"
    else:
        resultado = "impar"

    if resultado == adivinanza:
        print("Adivinaste correctamente mi perro")
    else:
        print("Adivinaste incorrectamente mi dog")
    
