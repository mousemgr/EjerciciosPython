
#Programa que calcula la Distancia de un
#punto (X1,Y1) a la recta Ax+By+C=0
import math

print("Programa que calcula la Distancia de un punto (X1,Y1) a la recta Ax+By+C=0")
print("======================================")
print("Localiza los Coeficientes A B y C en su Ec. Gral. de la recta")
A= int(input("Ingrese el valor de A: "))
B= int(input("Ingrese el vaLor de B: "))
C= int(input("Ingrese el valor de C: "))
print("\nIntroduzca el punto [X1,Y1]")
X= float(input("X1 = "))
Y= float(input("Y1 = "))

num = math.fabs(A*X+B*Y+C)
den = math.sqrt(A**2+B**2)
#den = math.hypot(A,B)
d=round(num/den,2)

print("\nLa distancia d es : ",d)