# @ficha : 2740559
# @autor : KEVIN YESID VASQUEZ CARTAGENA
# @fehca : 2023/10/05
#@descripcion : ejercicio de python

## import keyword
##
## print ("Hola mundo de python desde IDLE")
## print ("Las palabras reservadas de python:", keyword.kwlist)

#-------------------------------------------------------
# ejercicio 1:
var = 1
print (var)

raiz(x) = x ** 1/2
definir una variable 'x' con el valor raiz cubica de 27
x = 27 ** (1/3)
print ("La raiz cubica de 27 es :", x)
print (f"La raiz cubica de 27 es :{x}")


#-------------------------------------------------------
# ejercicio 2: resolver la ecuacion 3x^3 - 2x^2 + 5x - 3

para x = 0, x = 1, x = -1, x = 100
solucion :
x = 0
y = 3 * x ** 3 - 2 * x ** 2 + 5 * x -3
texto = "Solucion a la ecuacion  3x^3 - 2x^2 + 5x - 3 : "
print (texto, y)
print (f"La solucion a la ecuacion 3x^3 - 2x^2 + 5x - 3 con x = {x} es igual a {y}")

x = 1
y = 3 * x ** 3 - 2 * x ** 2 + 5 * x -3
texto = "Solucion a la ecuacion  3x^3 - 2x^2 + 5x - 3 : "
print (texto, y)
print (f"La solucion a la ecuacion 3x^3 - 2x^2 + 5x - 3 con x = {x} es igual a {y}")

x = -1
y = 3 * x ** 3 - 2 * x ** 2 + 5 * x -3
texto = "Solucion a la ecuacion  3x^3 - 2x^2 + 5x - 3 : "
print (texto, y)
print (f"La solucion a la ecuacion 3x^3 - 2x^2 + 5x - 3 con x = {x} es igual a {y}")

x = 100
y = 3 * x ** 3 - 2 * x ** 2 + 5 * x -3
texto = "Solucion a la ecuacion  3x^3 - 2x^2 + 5x - 3 : "
print (texto, y)
print (f"La solucion a la ecuacion 3x^3 - 2x^2 + 5x - 3 con x = {x} es igual a {y}")

#-------------------------------------------------------
# ejercicio 3: crear una credencia de presentacion con los siguientes datos
# nombres y apellidos completos, numero del celular, correo , redes sociales.
# datos almacenados en variables

name = "Kevin Yesid Vasquez Cartagena"
number = 3150870829
correo = "Kesvin200324@gmail.com"
cargo = "Estudiante"
red = "Kevin Vasquez"
fort = "Joder la vida"

print ("┌──────────────────────────────────────────┐")
print ("│                                          │")
print ("│  ■    ", name, "    │")
print ("│                                          │")
print ("│ ┼ Numero :", number, "                   │")
print ("│ ¢ Correo :", correo, "       │")
print ("│ ® Cargo :", cargo, "                    │")
print ("│                                          │")
print ("│         Redes Soiclaes                   │")
print ("│ ƒ Facebook :", red, "              │")
print ("│ ¥ Youtube :", red, "               │")
print ("│ $ Spotify :", red, "               │")
print ("│                                          │")
print ("│            Matriz Dofa                   │")
print ("│ ▀ Fortaleza :", fort ,"             │")
print ("│                                          │")
print ("└──────────────────────────────────────────┘")

#-------------------------------------------------------
# ejericio 4: calcular la hipotenusa de un trigualo rectangulo de dos lados
             3 y 4 respectivamente.
             hipotenusa : hps, Lado adyacente : la y lado opuesto : lo
la = 3
lo = 4
hps = la**2 + lo**2
print ("Hipotenusa es :", hps)
print (f"El lado adyacente : {la} y el lado opuesto : {lo}, con lo que la hipotenuza es igual a :",hps)


#-------------------------------------------------------
# ejercicio 5: realizar la conversion de pesos colombianos a dolares,
#              euros y viceversa a la tasa de cambio real

pesos = 20000
dolarP = pesos / 4382
euroP = pesos / 4612
dolarE = 4382 / 4612
euroD = 4612 / 4382

print ("")
print ("Ejercicio #5")
print (f"COP${pesos} equivalen a US${dolarP} dolares")
print (f"COP${pesos} equivalen a EU${euroP} euros")
print (f"US$1 equivalen a EU${dolarE}")
print (f"EU$1 equivalen a US${euroD}")

print ("COP $%d equivalen a US%.4f"% (pesos, dolarP))
print ("COP $%d equivalen a EU%.4f"% (pesos, euroP))
print ("EU$1 equivalen a US%.4f"% (euroD))
print ("US$1 equivalen a EU%.4f"% (dolarE))

print (f"COP${pesos} equivalen a US${dolarP:.4f}")
print (f"COP${pesos} equivalen a EU${euroP:.4f}")


#-------------------------------------------------------
# ejercicio 6: un automovil viaja a una velocidad de 120 km/h, calcular
#              la velocidad en m/h, km/s, m/s, mi/h y mi/s.
#              ¿Cual sera la distancia recorridad si el automovil viaja
#              a esa misma durante 3.5 horas ? calcular la distancia en m,km y mi

# conversiones de velocidad
velocidad_km_h = 120
velocidad_m_h = velocidad_km_h * 0.621371
velocidad_km_s = velocidad_km_h / 3600
velocidad_m_s = velocidad_km_s * 1000
velocidad_mi_s = velocidad_m_h / 3600

# distancia recorrida
tiempo_h = 3.5
distancia_km = velocidad_km_h * tiempo_h
distancia_m = distancia_km * 1000
distancia_mi = distancia_m / 1609.34

# imprimir resultados
print("Velocidad en m/h:", velocidad_m_h)
print("Velocidad en km/s:", velocidad_km_s)
print("Velocidad en m/s:", velocidad_m_s)
print("Velocidad en mi/s:", velocidad_mi_s)

print("Distancia recorrida en km:", distancia_km)
print("Distancia recorrida en m:", distancia_m)
print("Distancia recorrida en mi:",distancia_mi)


#-------------------------------------------------------
# explicacion de clase 

 funsion 'input()'
# ejemplo primera forma:
print ("Escribe algo...")
algo = input()
print (f"Mmm, {algo}, es en serio??")

# ejemplo segunda forma:
algo = input("Escribe algo: ")
print (f"Mmm, {algo}, es en serio??")

# ejemplo tercera forma (end):
print ("Escribe algo...", end = " ")
algo = input()
print (f"Mmm, {algo}, es en serio??")1321

#-------------------------------------------------------



#-------------------------------------------------------
# ejercicio 7: ficha con los siguientes datos (input)
# tipo de identificacion, identificacion, nombre, apellido
# fecha de nacimiento, edad, correo.
# Todos estos datos deben ser ingresados por teclado

tipo_identificacion = input("ingrese su tipo de identificacion : ")
identificacion = input("Ingrese su numero de identificacion : ")
nombres = input("Ingrese sus nombres : ")
apellidos = input ("ingrese sus apellidos : ")
fecha_nacimiento = input("ingrese su fecha de nacimiento : ")
edad = int(input("ingrese su edad : "))
correo = input("Ingrese su correo : ")

print ("┌────────────────────────────────────────────────┐")
print (f"""│     TIPO IDENTIFICACION: {tipo_identificacion:22s}│
│     IDENTIFICACION : {identificacion:26s}│
│     NOMBRE(s) : {nombres:31s}│
│     APELLIDO(s) : {apellidos:29s}│
│     FECHA NACIMIENTO : {fecha_nacimiento:24s}│
│     EDAD : {edad:36d}│
│     CORREO : {correo:34s}│""")
print ("└────────────────────────────────────────────────┘")

