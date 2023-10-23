# # @autor: Kevin Vasquez
# # @fecha: 2023/10/10
# # @descripcion: Manejo de ciclos y condicionales

# # ejercicio 1: ¿Cómo identificar el mayor de dos números?
# #               Los numeros deben ser ingresados por teclado
# #               Los numeros deben ser enteros
# # Leer los numeros
# numero1 = int (input ("Ingresa eI primer número") )
# numero2 = int (input ("Ingresa eI segundo número") )

# # elegir eI número más grande
# if numero1 > numero2 :
#     mayor = numero1
#     numero = "numero1"
# else :
#     mayor = numero2
#     numero = "numero2"

# # imprimir el resultado
# print (f"El número más grande: {mayor} y corresponde a la variable : {numero}")

# /----------------------------------------------------------------------------------------------------/

# # ejercicio 2: ¿Cómo identificar eI mayor de una secuencia de números?
# #               Contar el numero de valores ingresados
# #               Los numeros deben ser ingresados por teclado
# #               Los valores deben ser enteros

# # almacenamos el numero mas grande actual
# mayor = -999999999
# # inicializamos el contador
# contador_valores = 0

# #ingresar el primer valor 
# print("Programa que encuentra el numero mayor de una secuencia de numeros")
# print("Para termina ingrese -1")

# numero = int(input ("introduzca un número o ingrese -1 para terminar"))

# # si el número no es igual a —1, continuaremos
# while numero != -1:
#     # ingremento del contador
#     contador_valores += 1
#     # ¿ es el numero mas grande que se ha ingresado hasta el momento
#     if numero > mayor:
#         # actualizar el numero mayor
#         mayor = numero

#     # solicitar un nuevo numero o valor
#     numero = int(input ("introduzca un número o ingrese -1 para terminar"))

# # imprimir el resultado
# print(f"El numero mayor ingresado : {mayor} de un total de {contador_valores} valores ingresados")

# /----------------------------------------------------------------------------------------------------/

# ejercicio 3: ¿Cómo identificar el numero mayor y menor de una secuencia de números 
#               y calcular el promedio de una secuencia de numeros?
#               Contar el numero de valores ingresados
#               Los numeros deben ser ingresados por teclado
#               Los valores deben ser enteros

# # almacenamos el numero mas pequeño actualmente
# menor = 0
# # almacenamos el numero mas grande actualt
# mayor = -999999999
# # inicializamos el contador
# contador_valores = 0
# #inicializamos el promedio
# promedio = 0
# #inicializamos la suma
# suma = 0

# #ingresar el primer valor 
# print("Programa que encuentra el numero mayor, menor y el promedio de una secuencia de numeros")
# print("Para termina ingrese -1")

# numero = int(input ("introduzca un número o ingrese -1 para terminar"))

# # si el número no es igual a —1, continuaremos
# while numero != -1:

#     # ingremento del contador
#     contador_valores += 1
   
#     # ¿ es el numero mas grande que se ha ingresado hasta el momento
#     if numero > mayor:
#         # actualizar el numero mayor
#         mayor = numero
        
#     # ¿ es el numero mas pequeño que se ha ingresado hasta el momento
#     if numero < menor :
#         # actualizar el numero menor 
#         menor = numero

#     # se realiza la suma de todos los numeros ingresados
#     suma += numero

#     # solicitar un nuevo numero o valor
#     numero = int(input ("introduzca un número o ingrese -1 para terminar"))

# # despues de la suma dividimos por los valores ingresados para sacar un promedio 
# promedio = suma / contador_valores


# # imprimir el resultado
# print(f"El numero mayor ingresado : {mayor} de un total de {contador_valores} valores ingresados")
# print(f"El numero menor ingresado : {menor} de un total de {contador_valores} valores ingresados")
# print(f"El total de numeros digitados es de : {contador_valores}")
# print(f"El promedio es de : {promedio}")


# /----------------------------------------------------------------------------------------------------/

# ejercicio 4: Calcular la nómina de una secuencia de empleados de una empresa.
#            Se deben ingresar los siguientes datos por cada empleado:
#            identificacion, nombres, apellidos, correo, salario base.
#            Se deben calcular las deducciones por salud y pensión que
#            equivalen al 4% del salario base.
#            Si el salario neto calculado es menor de 1000000 se debe
#            agregar una comisión del 12% sobre el salario base.
#
#            Además, se debe calcular el promedio del salario base,
#            salud, pensión, salario neto y comisiones.
#            Por cada empleado se debe mostrar la información de la
#            siguiente forma:
#            +---------------------------------------+
#            | Empleado número: numero_del_empleado  |
#            +---------------------------------------+
#            | Idenfificación: identificacion        |
#            | Nombres: nombres y apellidos          |
#            | Correo: correo electronico            |
#            | Salario base: COP$salario base        |
#            | Salud: COP$salud                      |
#            | Pensión: COP$pension                  |
#            | Salario Neto: COP$salario neto        |
#            | Comisión: COP$comision                |
#            +---------------------------------------|
#              Salario base: COP$1,000,000.00

# Inicializamos variables para calcular el promedio
promedio_salario_base = 0
promedio_salud = 0
promedio_pension = 0
promedio_salario_neto = 0
promedio_comision = 0

# Solicitamos la cantidad de empleados
num_empleados = int(input("Ingrese el número de empleados: "))

contador_Empleados = 0  # Inicializamos el contador de empleados

while contador_Empleados < num_empleados:
    print(f"Empleado número: {contador_Empleados + 1}")
    identificacion = input("Identificación: ")
    nombre = input("Nombres: ")
    apellido = input("Apellidos: ")
    correo = input("Correo: ")
    salario = float(input("Salario base: COP$"))
    
    # Calculamos salud y pensión (4% del salario base)
    desc_salud = salario * 0.04
    desc_pension = salario * 0.04
    
    # Calculamos el salario neto
    salario_neto_empleado = salario - desc_salud - desc_pension
    
    # Si el salario neto es menor de 1000000, agregamos una comisión del 12%
    if salario_neto_empleado < 1000000:
        com = salario * 0.12
        salario_neto_empleado += com
    else:
        com = 0
    
    # Mostramos la información de cada empleado
    print(f"+---------------------------------------+")
    print(f"| Empleado número: {contador_Empleados + 1}")
    print(f"+---------------------------------------+")
    print(f"| Identificación: {identificacion}")
    print(f"| Nombres: {nombre} {apellido}")
    print(f"| Correo: {correo}")
    print(f"| Salario base: COP${salario:8,.2f}")
    print(f"| Salud: COP${desc_salud:2,.2f}")
    print(f"| Pensión: COP${desc_pension:2,.2f}")
    print(f"| Salario Neto: COP${salario_neto_empleado:8,.2f}")
    print(f"| Comisión: COP${com:.2f}")
    print(f"+---------------------------------------+")
    
    # Actualizamos las variables para el promedio
    promedio_salario_base += salario
    promedio_salud += desc_salud
    promedio_pension += desc_pension
    promedio_salario_neto += salario_neto_empleado
    promedio_comision += com
    
    contador_Empleados += 1  # Incrementamos el contador de empleados

# Calculamos el promedio dividiendo entre el número de empleados
promedio_salario_base /= num_empleados
promedio_salud /= num_empleados
promedio_pension /= num_empleados
promedio_salario_neto /= num_empleados
promedio_comision /= num_empleados

# Mostramos el promedio
print("\nPromedio:")
print(f"Salario base: COP${promedio_salario_base:.2f}")
print(f"Salud: COP${promedio_salud:.2f}")
print(f"Pensión: COP${promedio_pension:.2f}")
print(f"Salario Neto: COP${promedio_salario_neto:.2f}")
print(f"Comisión: COP${promedio_comision:.2f}")

# #  /--------------------------------------------------------------------------/
# ## primera forma
# # programa que lee una secuencia de numeros y cuenta cuantos numeros son pares
# #y cuantos son impares . El programa termina cuando se ingresa O

# contadorPares = 0
# contadorInpares = 0
# #lee el primer numero 
# numero = int(input("introdusca un numero  o escriba 0 para detener : "))

# # 0 termina la ejecucion  
# while numero !=0 : # se puede codificar de esta forma : while numero:
#     # verifica si el numero es impar 
#     if numero %2 ==1: 
#         contadorInpares +=1
#     else:
#         contadorPares += 1
#     numero = int(input("introdusca un numero o escriba 0 para detener: "))
# print(f" numeros pares: {contadorPares} .")
# print(f"numero impares: {int(contadorInpares)}.")


 
# # segunda forma 
# # programa que lee una secuencia de numeros y cuenta cuantos numeros son pares
# #y cuantos son impares . El programa termina cuando se ingresa O

# contadorPares = 0
# contadorInpares = 0
# #lee el primer numero 
# numero = int(input("introdusca un numero  o escriba 0 para detener : "))

# # 0 termina la ejecucion  
# while numero !=0 : # se puede codificar de esta forma : while numero:
#     # verifica si el numero es impar 
#     if numero < 1 :
#          # aumentar el contador de pares
          
#         contadorInpares +=1
    
#     else:
#         # aumentar el contador de impares 
#         contadorPares += 1
#      # leer el siguiente numero    
#     numero = int(input("ingrese un numero o escriba 0 para terminar: "))
    
#  # imprimir los resultados  
# print(f" numeros pares: {contadorPares} .")
# print(f"numero impares: {int(contadorInpares)}.")
