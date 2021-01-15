# Suma de Angulos Internos
# Conteo de Diagonales de un polígono

print("Programa que calcula angulos internos y Diagonales de un poligo de N Lados")

N = int(input("Introdusca el Número de lados del polígono a estudiar: "))

D = (N*(N-3))/2
S = 180*(N-2)

print("===========================================")
print("Número de lados de su Poligono: ",N)
print("Número de Diagonales: ",D)
print("Suma de Angulos Internos: ",S)