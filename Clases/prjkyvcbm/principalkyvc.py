# @autor : Kevin Yesid Vasquez
# @fecha : 19 octubre 2023
# @ficha : 2740559 
# @Description : programa principal el juego de buscaminas

# insercion de modulos propios para el buscaminas 
from modulobm import buscaminas as bm

print ("!Bienvenido al juego de buscaminas por consola ! ")
filas = int(input("Ingrese el numero de filas del tablero : "))
columnas = int(input("Ingrese el numero de columnas del tablero : "))

# creacion del tablero del buscaminas
tablerobm = bm.crear_tablero(filas, columnas)

# recorrido del tablero por indices 
for i in range (filas):
    print("[", end= " ")
    for j in range (columnas):
        print(f"{tablerobm[i][j]:2d}", end=", ")
    print ("]")