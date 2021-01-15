#Programa Calcula Calificacion

def calcula_calificacion(E,T,P):
    Cexamen = E*0.60
    Ctareas = T*0.10
    Cpracticas = P*0.30
    calif = (Cexamen + Ctareas + Cpracticas) 
    cf=round(calif,1)
    print("Evaluación Final: ",cf)
    if(cf>9):
        print("Sobresaliente")
    elif(cf>8):
        print("Notable")
    elif(cf>7):
        print("Bien")
    elif(cf>6):
        print("Suficiente")
    else:
        print("Insuficiente")

Name = input("Nombre del Estudiante: ")
Examen = float(input("Examen = "))
Tareas = float(input("Tareas = "))
Practica = float(input("Pract. = "))

calcula_calificacion(Examen,Tareas,Practica)