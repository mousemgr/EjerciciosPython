#Ruleta con numeros aleatorios
Alumnos = ["Israel","Gustavo","Sara","Ángel","Rosa","Brenda"
           ,"Stephany","Juan Carlos"]

import random as rd

#i = round(rd.random()*7)
#i = rd.randint(0,7)
#print(Alumnos[i])
i = rd.choice(Alumnos)
print(i)