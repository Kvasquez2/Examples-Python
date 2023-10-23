# @autor : Kevin Yesid Vasquez
# @fecha : 19 octubre 2023
# @ficha : 2740559 
# @Description : funciones para el back-end and front-end del juego de buscaminas

# modulos propios de python
import math
import random
import os 

# valor de la mina 
MINA = -1

# Snikes
# funciones del back-end para el juego de buscaminas 
# Funcion para crear el tablero de buscaminas 
def crear_tablero (nro_filas, nro_columnas, porc_minas =30):
    # crear po comprension la lista el tablero de buscaminas
    tablero = [[0 for j in range (nro_columnas)]for i in range (nro_filas)]

    insertar_minas(tablero, porc_minas)

    #conteo_minas(tablero)
    conteo_minas_izquierda(tablero)
    # conteo_minas_derecha(tablero)
    conteo_minas_superior(tablero)
    # conteo_minas_inferior(tablero)
    conteo_minas_esquina_superior_izquierda(tablero)

    return tablero


# funcion para insertar las minas en el tablero en el tablero 
def insertar_minas(tablero, porc_minas):
    # definir el condtador de minas 
    cont_minas = 0
    # calcular el nro de minas a insertar en el tablero 
    filas = len(tablero)
    columnas = len(tablero[0])
    nro_minas = math.ceil(filas * columnas * (porc_minas / 100))

    while cont_minas < nro_minas:
        # elegir una fila y columna al azar
        fila = random.randrange(0, filas )
        columna = random.randrange(0, columnas)

        # preguntamos si la celda elegido aun no contiene minas 
        if tablero [fila][columna] != MINA:
            tablero[fila][columna] = MINA
            cont_minas +=1
        else:
            continue



# funcion para el conteo de minas alrededor para cada una de las celdas
def conteo_minas(tablero):
    # realizar el recorrido sobre el tablero por indice
    filas = len(tablero)
    columnas = len(tablero[0])

    for i in range(1, filas - 1):
        for j in range (1, columnas - 1):
            if tablero [i][j] != MINA:
                if tablero [i - 1][j - 1] == MINA:
                    tablero[i][j] += 1
                if tablero [i - 1][j] == MINA:
                    tablero[i][j] += 1
                if tablero [i - 1][j + 1] == MINA:
                    tablero[i][j] += 1
                if tablero [i][j - 1] == MINA:
                    tablero[i][j] += 1
                if tablero [i][j + 1] == MINA:
                    tablero[i][j] += 1
                if tablero [i + 1][j - 1] == MINA:
                    tablero[i][j] += 1
                if tablero [i + 1][j] == MINA:
                    tablero[i][j] += 1
                if tablero [i + 1][j + 1] == MINA:
                    tablero[i][j] += 1



# funcion para hallar las minas en el extremo izquierdo 
# sin tener en cuenta la esquina superior izquierda 
# y la esquina inferior izquierda
def conteo_minas_izquierda(tablero):
    filas = len(tablero)
    for i in range(1, filas - 1):
        if tablero [i][0] != MINA:
            if tablero [i - 1]  [0] == MINA:
                tablero[i]      [0] +=1
            if tablero [i - 1]  [1] == MINA:
                tablero[i]      [0] +=1
            if tablero [i]      [1] == MINA:
                tablero[i]      [0] +=1
            if tablero [i + 1]  [0] == MINA:
                tablero[i]      [0] +=1
            if tablero [i + 1]  [1] == MINA:
                tablero[i]      [0] +=1



# funcion para hallar las minas en el extremo derecho
# sin tener en cuenta la esquina superior derecha 
# y la esquina inferior derecha
def conteo_minas_derecha(tablero):
    filas = len(tablero)
    for i in range(1, filas - 1):
        if tablero [i][-1] != MINA:
            if tablero [i - 1]    [-1] == MINA:
                tablero[i]        [-1] +=1
            if tablero [i - 1]    [-2] == MINA:
                tablero[i]        [-1] +=1
            if tablero [i]        [-2] == MINA:
                tablero[i]        [-1] +=1
            if tablero [i + 1]    [-1] == MINA:
                tablero[i]        [-1] +=1
            if tablero [i + 1]    [-2] == MINA:
                tablero[i]        [-1] +=1



# funcion para hallar las minas lo supe
# sin tener en cuenta la esquina superior derecha 
# y la esquina inferior derecha
def conteo_minas_superior(tablero):
    columnas = len(tablero[0])
    for j in range(1, columnas - 1):
        if tablero [0]  [j] != MINA:
            if tablero [0]      [j - 1]== MINA:
                tablero[0]      [j] +=1
            if tablero [0]      [j + 1] == MINA:
                tablero[0]      [j] +=1
            if tablero [1]      [j - 1] == MINA:
                tablero[0]      [j] +=1
            if tablero [1]      [j] == MINA:
                tablero[0]      [j] +=1
            if tablero [1]      [j + 1] == MINA:
                tablero[0]      [j] +=1



# funcion para hallar las minas lo supe
# sin tener en cuenta la esquina superior derecha 
# y la esquina inferior derecha
def conteo_minas_inferior(tablero):
    columnas = len(tablero[0])
    for j in range(1, columnas - 1):
        if tablero [-1]  [j] != MINA:
            if tablero [-1]      [j - 1]== MINA:
                tablero[-1]      [j] +=1
            if tablero [-1]      [j + 1] == MINA:
                tablero[-1]      [j] +=1
            if tablero [-2]      [j - 1] == MINA:
                tablero[-1]      [j] +=1
            if tablero [-2]      [j] == MINA:
                tablero[-1]      [j] +=1
            if tablero [-2]      [j + 1] == MINA:
                tablero[-1]      [j] +=1



# funcion para hallar las minas lo supe
# sin tener en cuenta la esquina superior derecha 
# y la esquina inferior derecha
def conteo_minas_esquina_superior_izquierda(tablero):
    filas = len(tablero)
    for i in range(1, filas):
        if tablero [i][0] != MINA:
            if tablero [i]      [1] == MINA:
                tablero[i]      [0] +=1
            if tablero [i + 1]      [1] == MINA:
                tablero[i]      [0] +=1
            if tablero [i + 1]      [1] == MINA:
                tablero[i]      [0] +=1
