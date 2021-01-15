#Calculo del área y perímetro de un círculo
import math

print("Calculadora de A y P de una circunferencia")

r = float(input("Ingrese el radio de la Circunferencia: "))

A = math.pi*r**2; A = round(A,2)
P = 2*math.pi*r;  P = round(P,2)

print("El área del Círculo es: ", A)
print("El Perímetro del Círculo es: ",P)