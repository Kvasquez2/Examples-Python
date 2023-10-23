# # @autor: Kevin Vasquez
# # @fecha: 2023/10/10
# # @descripcion: Manejo de ciclos y condicionales

# ejercicio: impromir los 10 primeros numeros enteros positivos

# # primero forma del ciclo para (for)
# print ("Imprimir los 10 primeros numeros enteros positivos ...")
# for i in range (10)
#     print(f"numero : {i}")


#segunda forma del ciclo para (for)
# contadorValores = 0
# for i in range (-5, 0):
#     contadorValores += 1
#     print(f"Numero : {i}")
    
# print(f"Se realializaron {contadorValores} iteraciones del ciclo para")

# # tercera forma del ciclo para (for)
# for i in range (-3, 8,2):
#     contadorValores += 1
#     print(f"numero : {i}")

# print(f"Se realializaron {contadorValores} iteraciones del ciclo para")

# / ---------------------------------------------------------------------/

# ejercicio 2: generar e imprimir la serie de fibonaccio
# para los primeros 20 valores
# fibonacci : 0 ,1 ,1 ,2 ,3 ,5 ,8 ,13, ...

# Inicializamos los primeros dos términos de la serie
# anterior , presente= 0, 1

# print(f"1 :      {anterior}\n 2 :     {presente}")
# # # Imprimimos los primeros 30 términos de la serie de Fibonacci
# for i in range(2, 30):
#     fibo = anterior + presente
#     print (f"{i+1:3d} : {fibo:6d}")
#     anterior = presente
#     presente = fibo


# / ---------------------------------------------------------------------/
# Ejericicio 3: escribir un ciclo for que cuente hasta cinco
# cuerpo del ciclo : imprimir el numero de iteracion
# del ciclo y la palabra "mississippi"
# Cuepo del ciclo - uso de la funcion time.sleep(1)
# Escribir una funsion de impresion con el mensaje final :
# "! Listo o no, ahi voy!".

# import : palabra que me permite utilizar modulos (paquetes o librerias)
#           propios de python, de terceros o personalizados

# import time

# # Ciclo for que cuenta hasta cinco
# for i in range(1, 6):
#     print(f"Iteración {i}: Mississippi")
#     time.sleep(1)  # Pausa de 1 segundo

# time.sleep(1)  # Pausa de 1 segundo
# print("! Listo o no, ahí voy!")


# / ---------------------------------------------------------------------/
# # break - ejemplos (roptura. romper o quebrar)
# print("La instrucion break (ruptura)")
# for i in  range (1,6):
#     if i ==3:
#         print("Saliendo del ciclo ...")
#         break
#     print(f"{i} iteracion del ciclo for ...")

# print ("por fuera del ciclo...")

# # continue - ejemplo 
# print("La instrucion continue (ruptura)")
# for i in  range (1,6):
#     if i ==3:
#         print("Me salto esta iteracion")
#         continue
#     print(f"{i} iteracion del ciclo for ...")

# print ("por fuera del ciclo...")

# # ejemplo: devorador de vocales
# palabra_usuario = input("ingrese una palabra :")
# palabra_usuario = palabra_usuario.upper()
# palabra_sin_vocales = ""

# for letra in palabra_usuario:
#     if letra == "A": continue
#     elif letra == "E": continue
#     elif letra == "I": continue
#     elif letra == "O": continue
#     elif letra == "U": continue
#     else: palabra_sin_vocales += letra

# print(f"Palabra sin vocales : {palabra_sin_vocales}")

# /--------------------------------------------------------------------------/

# ejericicio 4: 
# generar un valor aleatorio entre 0 y 1000 para el numero secreto
# cuando el usuario ingrese un numero se le debe de dar una indicacion de si el numero secreto
# esta por ensima o por debajo del numero ingresado, con la frase : 
# "El numero secreto es mayor" o "El numero secreto es menor"
# el usuario va a tener maximo 8 oportunidades para divinar el numero secreto, 
# de lo contrario se termina el juego con la frase : " Lo siento muggle no has adivinado el numero"

# # El número secreto del mago
# secret_number = 7

# # Pedir al usuario que ingrese un número entero
# user_number = int(input("Adivina el número secreto del mago (un número del 1 al 10): "))

# # Iniciar un bucle while para el juego
# while user_number != secret_number:
#     print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
#     user_number = int(input("Inténtalo de nuevo: "))

# # Si el usuario adivina el número, mostrar un mensaje de felicitación
# print("¡Bien hecho, muggle! Eres libre ahora. El número secreto era 7.")



# /------------------------------------------------------------------------------/

# /-------------------------------- Listas---------------------------------------/

# /------------------------------------------------------------------------------/

# ejercicio: listas
# Habia una vez un sombrero.  El sombrero no contenia conejo, sino
# una lista de cinco numeros : 1 ,2 ,3 ,4 ,5
# Escribir una Línea de código que solicite al usuario que remplace
# eL número central en La Lista con un número entero ingresado por éste
# Escribir una Línea de código que elimine el último elemento de La list
#- Escribir una Línea de código que imprima La longitud de La Lista existente

# # crear la Lista por extensión:
# numeros = [1,2,3,4,5]
# # crear La Lista por comprensión:
# numeros_comprension = [i for i in range(1 , 6)]

# print(f"lista 1: {numeros}\nLista 2: {numeros_comprension}")
# numeros[2] = int(input("Ingrese un numero entero :"))
# print(f"Lista modificada : {numeros}")

# del numeros [-1]

# print(f"Lista modificada : {numeros}")
# print(f"La longitud de la lista es : {len(numeros)}")

# # eliminar el primer elemento de la lista "numeros_comprension"
# del numeros_comprension[-len(numeros_comprension)]
# print (f"Lista 2 modificada : {numeros_comprension}")
# print (f"Ultimo elemento en forma normal : {numeros[len(numeros) -1 ]}")



# codigo con las otras tres indicaciones 
import random

# Generar un número secreto aleatorio entre 100 y 1000
number_secret = random.randint(0, 1000)

# Inicializar el número de intentos
intentos = 0
maximos_intentos = 8

# Mostrar un mensaje de bienvenida
print("╔═════════════════════════════════════════════════════════════════════════╗")
print("║                  Bienvenido a mi juego, Muggle!                         ║")
print("║    Introduce un número entero y adivina que número he elegido para tu.  ║")
print("║       Estoy pensando en un número entre 0 y 1000. Adivina cuál es.      ║")
print("║                 Tienes 8 oportunidades para adivinarlo.                 ║")
print("║                   ¡Cual va hacer ese numero secreto ?                   ║")
print("╚═════════════════════════════════════════════════════════════════════════╝")

# Iniciar un bucle while para el juego
while intentos < maximos_intentos:
    print("╔════════════════════════════╗")
    NumeroUsuario = int(input("║     Digita el número:"))
    print("╚════════════════════════════╝")

    # Incrementar el número de intentos
    intentos += 1

    if NumeroUsuario < number_secret:
        print("╔══════════════════════════════════════════════════════════════════════╗")
        print("║                  El número secreto es mayor                          ║")
        print("║             El numero es mayor que el ingresado                      ║")
        print(f"║                intentos: {intentos}                                           ║")
        print("╚══════════════════════════════════════════════════════════════════════╝")
    elif NumeroUsuario > number_secret:
        print("╔══════════════════════════════════════════════════════════════════════╗")
        print("║                  El número secreto es menor                          ║")
        print("║             El numero es menor que el ingresado                      ║")
        print(f"║                intentos: {intentos}                                           ║")
        print("╚══════════════════════════════════════════════════════════════════════╝")
    else:
        print(f"¡Felicidades! Has adivinado el número secreto ({number_secret}).")
        break

# Comprobar si el usuario ha agotado los intentos
if intentos == maximos_intentos:
    print("╔═════════════════════════════════════════════════════════════╗")
    print("║         Lo siento, muggle. No has adivinado el número       ║")
    print(f"║                  El número secreto es : {number_secret}                 ║")
    print("╚═════════════════════════════════════════════════════════════╝")