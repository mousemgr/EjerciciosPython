#ESTATURAS DE 1000 ALUMNOS DE PREPARATORIA
import matplotlib.pyplot as mpl
import numpy as np
mpl.close("all")

alturas = np.random.uniform(150,185,1000)
#alturas = np.random.normal(150,185,1000)

#bins = Numero de grupos en que se repartira la muestra
mpl.figure(1)
mpl.title("Estatura de 100 alumnos de Preparatoria")
mpl.hist(alturas, bins=7, color="C9", edgecolor="black")
mpl.xlabel("Estatura en cm")
mpl.ylabel("Cantidad de alumnos ")