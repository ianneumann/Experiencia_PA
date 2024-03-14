import random 
def adivinar_par_o_impar():
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """

    adivinanza = int(input("Ingrese 1 si cree que el número va a ser impar y 2 si es par: "))
    numero = random.randint(1,100)

    if numero %2 == 0 and adivinanza == 2:
        print("Adivinaste! Dijiste que era par y salio el numero " + str(numero))

    elif numero %2 != 0 and adivinanza == 1:
        print("Adivinaste! Dijiste que era impar y salio el numero " + str(numero))

    elif numero %2 == 0 and adivinanza == 1:
        print("Rayos te equivocaste! Dijiste que era impar y salio el numero " + str(numero))

    elif numero %2 != 0 and adivinanza == 2:
        print("Rayos te equivocaste! Dijiste que era par y salio el numero " + str(numero))

    else:
        print("DEBES ELEGIR SOLO LA OPCION 1 O 2")
    pass
