#Bucle Infinito. continue y break
while True:
    linea = input(">>") #Requisitar deatos del usuario
    linea2 = linea.lower() #convierte la cadena a minusculas (.upper())
    if (linea2 == "fin"): break #rompeciclos
    if (linea[0] == "#"): continue #Saltar a la sig iteración
    print(linea)
print("Terminado")