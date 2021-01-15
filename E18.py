#Ventas Inmobiliaria (entre 2000,2020)
import matplotlib.pyplot as mpl
import numpy as np
mpl.close("all")

ventas = np.array(([45,56,78,47,56,45,78,69,68,54,45]))
years  = np.linspace(2000,2020,11)

mpl.figure(1)
mpl.title("Bienes Raices SA de CV")
mpl.grid()
mpl.xlim(1995,2025)
mpl.ylim(0,90)
mpl.xlabel("Años")
mpl.ylabel("No. de Propiedades Vendidas")
mpl.plot(years,ventas)
mpl.scatter(years,ventas)