import random

def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """

    num = random.randint(1,10)
    resp = int(input('Adivina el numero del 1 al 10 oh usuario rey: '))

    if resp == num:
        print('Hurra! Lo haz hecho de maravilla (como siempre)')
    else:
        print('Hoy no es tu dia')
    
    