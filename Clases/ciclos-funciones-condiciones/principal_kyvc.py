# @autor: Kevin Yesid Vasquez Cartagena
# @fecha : 17 octubre 2023
# @ficha : 2740559
# @ descripcion : Programa principal que utiliza un modulo-paquete o librerio personalizada

import funciones_kyvc as funciones

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
    total52, sumando1 , sumando2 = funciones.sumar_forma_52(op1 , op2)
else :
    total52, sumando1 , sumando2 = funciones.sumar_forma_52(op1)

print(f"La suma de {sumando1} + {sumando2} es : {total52}")


# actividad
# Desarrollar un programa para realizar operaciones matematicas 
# suma, resta, multiplicacion, divicion, reciduo, y potencia
# utilizando un modulo llamado : 'modulo_xxxx' y llamando las respectivas funciones
# y debe contener un menu con las diferentes opciones que tambien es una funcion invocada desde el programa principal
# ademas va a tener otro submenu del calculo de las areas y los perimetros de : triangulo rectangulo, rectangulo, circulo, cuadrado