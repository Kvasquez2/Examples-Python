# @autor: Kevin Yesid Vasquez Cartagena
# @fecha : 17 octubre 2023
# @ficha : 2740559
# @ descripcion : Definicion y ejecucion de funciones

# funcion : es un tarea pequeña, de varios renglones se usa para modularizar un programa
#            en partes mas pequeñas de forma que se pueda modificar con facilidad y  se 
#           pueda reconocer y corregir errores en el codigo.
#           LAs funciones cuando estan orientadas a objetos se llaman (metodos o comportamientos)
#           LAs funciones cunado estan en algoritmia se llaman (subprocesos)
#           Las funciones secuenciales se llaman (funciones o subrutinas)

#           Una funcion se reconoce de una varibañe porque tiene ().
#           tiene parametros : de entrada son los que estan dentro de los parentesis, y tiene de salida

#           Existen 4 tipos de funciones :
#           1. sin pareametro de entrada y sin parametros de salida 
#           2. sin parametros de entrada y con parametros de salida
#           3. con parametros de entrada y sin parametros de salida
#           4. con parametros de entrada y con parametros de salida

# Definicion de una funcion en python:
#   def nombre_funcion(paramm1, param2, ... paramn) :    Simpre debe de estar separado por comas y es opcional [] dentron de los parentesis encerrado los parametros
#       cuerpo_de_la_funcion
#       [return valor]

# crear una funcion para realizar la suma de dos numeros enteros
# 1. primera forma : sin parametros de entrada y sin parametros de salida 

def sumar_forma_1 ():
    """
        Funcion que realiza la suma de numeros enteros
    """
    # definir dos variables y capturar los datos por teclado 
    op1 = int(input("Ingrese el primer numero :´"))
    op2 = int(input("Ingrese el segundo numero :"))
    total = op1 + op2
    print (f"El total de {op1} + {op2} es : {total}")


# 2. segunda forma : sin parametros de entrada y con parametros de salida
def sumar_forma_2 ():
    """
        Funcion que realiza  la suma de numeros enteros
        parametro de salida : un total de tipo entero (int)
    """
    # definir dos variables y retornar el resultado 
    op1 = int(input("Ingrese el primer numero :´"))
    op2 = int(input("Ingrese el segundo numero :"))
    total = op1 + op2

    return total


# 3. Tercera forma : con parametros de entra y sin parametros de salida
def sumar_forma_3 (op1, op2):
    """
        Funcion que realiza  la suma de numeros enteros
        parametro de entrada : op1 y op2 tipo entero (int)
    """
    total = op1 + op2
    print (f"El total de {op1} + {op2} es : {total}")


# 4. Cuarta forma: Con parametros de entrada y con parametos de salidad (llamdo como caja negra)
def sumar_forma_4(op1,op2): #op1 = es operador nombre para la suma
    """
        Funcion que realiza  la suma de numeros enteros
        parametro de entrada y de salida : op1, op2 y total tipo entero (int)
    """
    total = op1 + op2
    return total
    # return total = op1 + op2
    # return op1 + op2


# 5. quinta forma: con retorno de varios parametros
def sumar_forma_5(op1, op2):
    """
        Funcion que realiza  la suma de numeros enteros
        parametro de entrada y varios parametros de salida
    """
    total = op1 + op2
    return total, op1, op2


# 5.1: quinta y primera forma : con parametros de entrada opcionales
#       un solo parametro de salida
def sumar_forma_51(op1, op2 = 50):
    """
        Funcion que realiza  la suma de numeros enteros
        1 parametro de entrada y otro parametro opcional
    """
    total = op1 + op2
    return total


# 5.2 Quinta y segundo forma: con parametros opcinales y varios parametros de salida
def sumar_forma_52(op1, op2 = 50):
    """
        Funcion que realiza  la suma de numeros enteros
        1 parametro de entrada y otro parametro opcional y con varios parametros de salida
    """
    total = op1 + op2
    return total, op1, op2


# programa principal
# Realiza la suma de dos numeros utilizando funciones 
print ("Programa que realiza la suma de dos numeros enteros")

# # # utilizando la funcion 'sumar_forma_1()'
# print ("Utilizando la funcion 'sumar_fomra_1'")
# sumar_forma_1()

# # utilizando la funcion 'sumar_forma_2()'
# print ("Utilizando la funcion 'sumar_fomra_2'")
# total2 = sumar_forma_2()
# print (f"El total es : {total2}")
# print (f"El total es : {sumar_forma_2()}")

# # utilizando la funcion 'sumar_forma_3(op1, op2)'
# #   primera forma
# print("Utiulizando la funcion 'sumar_forma_3(param1, param2)")
# sumar_forma_3(45,35)

# #   segunda forma
# op1 = int(input("Ingrese el primer numero : "))
# op2 = int(input("Ingrese el segundo numero :"))
# sumar_forma_3(op1,op2)


# # utilizando la funcion 'sumar_forma_4(param1, param2)'
# #   primera forma
# print("Utiulizando la funcion 'sumar_forma_4(param1, param2)")
# total4 = sumar_forma_4(45,38)
# print(f"El total es : {total4}")

# #   segundo forma
# op1 = int(input("Ingrese el primer numero : "))
# op2 = int(input("Ingrese el segundo numero :"))
# total41 = sumar_forma_4(op1, op2)
# print (f"El total es : {total41}")
# # segunda forma de la segunda forma
# print(f"el total es : {sumar_forma_4(op1,op2)}")


# # retorno de varios parametros
# print("Utilizando una funcion que retorna varios parametros ...")
# op1 = int(input("Ingrese el primer numero : "))
# op2 = int(input("Ingrese el segundo numero :"))
# total5, sumando1, sumando2 = sumar_forma_5 (op1, op2)
# print (f"La suma de {sumando1} + {sumando2} es : {sumar_forma_5}")


# # invocando una funcion con parametro opcional
# print("Utilizando una funcion con parametro opcional")
# op1 = int(input("Ingrese el primer numero : "))
# op2 = int(input("Ingrese el segundo numero : "))
# if op2 >= 0:
#     total51 = sumar_forma_51(op1 , op2)
# else :
#     total51 = sumar_forma_51(op1)

# print(f"El total es : {total51}")


# invocando una funcion con parametro opcional
# y con varios parametos de salida
print("""Utilizando una funcion con parametro opcional 
      y varios parametros de salida""")
op1 = int(input("Ingrese el primer numero : "))
op2 = int(input("Ingrese el segundo numero : "))
if op2 >= 0:
    total52, sumando1 , sumando2 = sumar_forma_52(op1 , op2)
else :
    total52, sumando1 , sumando2 = sumar_forma_52(op1)

print(f"La suma de {sumando1} + {sumando2} es : {total52}")