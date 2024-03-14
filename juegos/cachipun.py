import random

def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    #c es computadora y u es usuario
    c = random.randint(1,3)
    if c == 1:
        c = 'piedra'
    elif c == 2:
        c = 'papel'
    else:
        c = 'tijera'

    u = str(input('Elegir piedra, papel o tijera! '))

    print(f'El computador saco {c} y el usuario saco {u}!')
    '''a ver a ver'''

