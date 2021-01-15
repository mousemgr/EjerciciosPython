#Ejercicio Temperatura
import math

To = 120
Ts = 38
k  = 0.45
t  = 4

T = Ts + (To-Ts)*math.exp(-k*t)
T =round(T)

print("La temperatura despues de ese tiempo será de[F]: ",T)