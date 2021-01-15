# Aplicación Estadistica
suma = 0; contador = 0
while True:
    linea = input(">>")
    if(linea.lower()=="fin"):
        break
    i = float(linea)
    suma = suma + i #Suma de los num de entrada
    contador = contador + 1 #Contador de elementos
    media = suma/contador
print("# elementos:",contador)
print("sum elem.:",suma)
print("media de los datos:",media)
    