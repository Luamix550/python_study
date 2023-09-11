#!/usr/bin/env python3
import time

print("¡Bienvenido a la calculadora basica!, por favor escoja que operador aritmetico desea usar:")

operador = input("Escoja su operador aritmetico: +, -, *, /: ")

numero1 = float(input("Introduce el primer numero:"))
numero2 = float(input("Introduce el Segundo numero:"))

time.sleep(3)
if operador == "+":
    print(numero1 + numero2)
    
elif operador == "-":
    print(numero1 - numero2)
elif operador == "*":
    print(numero1 * numero2)
elif operador == "/":
    if numero2 ==0:
        print("ZeroDivisionError")
    else:
        print(numero1/numero2)
        
salir = input("Desea salir? (si/no): ").lower()
if salir == "si":
    print("¡Hasta luego!")
    exit()