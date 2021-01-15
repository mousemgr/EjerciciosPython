#Funciones en python

def suma(a,b):
    R=a+b
    print("El Resultado de la suma es: ",R)
def resta(a,b):
    R=a-b
    print("El Resultado de la resta es: ",R)
def producto(a,b):
    R=a*b
    print("El Resultado del producto es: ",R)
def cociente(a,b):
    R=a/b
    print("El Resultado del cociente es: ",R)
def potencia(a,b):
    R=a**b
    print("El Resultado de la potencia a^b es: ",R)
def mod(a,b):
    R=a%b
    print("El Resultado del modulo [residuo] es: ",R)

print("Calculadora Arítmetica [+,-,*,/,**,%]")
a = float(input("A = "))
b = float(input("B = "))

suma(a,b)
resta(a,b)
producto(a,b)
cociente(a,b)
potencia(a,b)
mod(a,b)