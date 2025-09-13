# Problema 1

nombre = input("Ingresa tu nombre: ")
print("¡Hola " + nombre + "!")


# Problema 2

consumo = float(input("¿Cuánto fue tu consumo? "))
propina = float(input("¿Qué porcentaje de propina deseas dejar? "))
monto_propina = consumo * (propina / 100)
print("Debes dejar una propina de:", monto_propina)


# Problema 3

payasos = int(input("Número de payasos vendidos: "))
munecas = int(input("Número de muñecas vendidas: "))
peso_total = (payasos * 112) + (munecas * 75)
print("El peso total del paquete es:", peso_total, "gramos")


# Problema 4

N = int(input("Introduce un número entero positivo: "))
suma = 0
for i in range(1, N+1):
    suma = suma + i
print("La suma es:", suma)


# Problema 5

shows = int(input("¿Cuántos shows viste este año? "))
if shows > 3:
    print(True)
else:
    print(False)


# Problema 6

edad = int(input("¿Cuál es tu edad? "))
if edad < 4:
    print("Entrada gratis")
elif edad >= 4 and edad <= 18:
    print("El precio es $5")
else:
    print("El precio es $10")


# Problema 7

a = float(input("Primer número: "))
b = float(input("Segundo número: "))

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")

op = input("Elige una opción: ")

if op == "1":
    print("Resultado:", a + b)
elif op == "2":
    print("Resultado:", a - b)
elif op == "3":
    print("Resultado:", a * b)
else:
    print("Opción inválida")


# Problema 8

time = input("Ingresa la hora (HH:MM): ")
hours, minutes = time.split(":")
hora = int(hours) + (int(minutes) / 60)

if hora >= 7 and hora <= 8:
    print("Es hora de desayunar")
elif hora >= 12 and hora <= 13:
    print("Es hora de almorzar")
elif hora >= 18 and hora <= 19:
    print("Es hora de cenar")


# Problema 9

deposito = float(input("Cantidad depositada: "))
tasa = 0.04

año1 = deposito * (1 + tasa)
año2 = año1 * (1 + tasa)
año3 = año2 * (1 + tasa)

print("Ahorros después de 1 año:", round(año1, 2))
print("Ahorros después de 2 años:", round(año2, 2))
print("Ahorros después de 3 años:", round(año3, 2))


# Problema 10

import math

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

discriminante = b**2 - 4*a*c

if a == 0:
    if b == 0:
        print("Ecuación no presenta solución real")
    else:
        x = -c / b
        print("Solución única:", x)
else:
    if discriminante < 0:
        print("Ecuación no presenta solución real")
    elif discriminante == 0:
        x = -b / (2*a)
        print("Solución única:", x)
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print("Dos soluciones:", x1, "y", x2)
        
        