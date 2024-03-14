import random

def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    dif = str(input('Elegir dificultad: facil/medio/dificil '))
    if dif == 'facil':
        dif = 3
    elif dif == 'medio':
        dif = 5
    else:
        dif = 10
    print('Iniciando la secuencia...')
    sec_c = []
    for i in range(dif):
        num = random.randint(1,10)
        sec_c.append(num)
    print(sec_c)

    sec_u = []
    for i in range(dif):
        num = int(input('Insertar numero: '))
        sec_u.append(num)

    if sec_c == sec_u:
        print('Enhorabuena! Eres el repetidor de secuencias johnson')
    else:
        print('Hace falta entrenar la memoria broski')