#Comprobar una Identidad Trigonométrica
import math

alpha = 5*math.pi/9
betha = math.pi/7

a = math.cos(alpha) - math.cos(betha)

b = 2*math.sin(0.5*(alpha+betha))*math.sin(0.5*(betha-alpha))

a=round(a,6); b=round(b,6)
print(a)
print(b)

if (a==b): print("Se comprueba la Identidad")
else: print("No se comprueba la identidad [a!=b]")