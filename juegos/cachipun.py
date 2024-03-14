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
    if (c == 'piedra' and u == 'tijera') or (c == 'papel' and u == 'piedra') or (c == 'tijera' and u == 'papel'):
        print('Perdiste cabeza de chorlito!')
    elif (u == 'piedra' and c == 'tijera') or (u == 'papel' and c == 'piedra') or (u == 'tijera' and c == 'papel'):
        print('Has ganao!')
    elif u == c:
        print('Es un empate')

