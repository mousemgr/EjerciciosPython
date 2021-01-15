suma = 0; pares = 0; nones = 0
for i in range(101):
    suma = suma + i
    if (i%2==0): pares = pares + i
    else: nones = nones +i 
print("La suma de todos los elementos resulta en : ", suma)
print("Suma de pares: ",pares)
print("Suma de Impares: ",nones)
