print("Programa que clasifica Generaciones")

year = int(input("Ingrese su año de nacimiento = "))
msj1 = "Usted pertenece a la Generación"
msj2 = "=================================="

if (year>=1946 and year<=1964):
    print(msj2)
    print("Año de nacimiento: ",year)
    print(msj1, "Baby Boomers")
elif (year>=1965 and year<=1980):
    print(msj2)
    print("Año de Nacimiento: ",year)
    print(msj1, "X")
elif (year>=1981 and year<=2000):
    print(msj2)
    print("Año de Nacimiento: ",year)
    print(msj1, "Y. Millenials")
elif (year>=2001):
    print(msj2)
    print("Año de Nacimiento: ",year)
    print(msj1, "Z. Boomlets")
else:
    print(msj2)
    print("Año de Nacimiento: ",year)
    print("No tiene asignada ninguna generación especifica")

print("Hasta la Próxima")

