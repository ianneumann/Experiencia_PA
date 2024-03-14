import random 
def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """

    puntos_usuario = 0
    puntos_compu = 0
    turno = 0

    while puntos_usuario<30 and puntos_compu<30:
        if turno == 0:
            lanzar_dado = input('apreta enter para tirar el dado:')
            numero = random.randint(1,6)
            print("Te salio el numero " + str(numero))
            puntos_usuario += numero
            print("Puntos usuario: " + str(puntos_usuario))
            print("Puntos computador: " + str(puntos_compu))            
            turno = 1

        elif turno == 1:
            print("Es el turno del computador")
            numero = random.randint(1,6)
            print("Al computador le salio el numero " + str(numero))
            puntos_compu += numero
            print("Puntos usuario: " + str(puntos_usuario))
            print("Puntos computador: " + str(puntos_compu))            
            print("Es el turno del usuario")
            turno = 0      
    
    if puntos_usuario > puntos_compu:
        print("Felicidades! Has Ganado")

    else:
        print("MUAAJJAAJAJAJAJ! El computador es mas poderoso que el hombre XD")
    pass