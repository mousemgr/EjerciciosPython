import matplotlib.pyplot as mpl
import numpy as np
import math
mpl.close("all")

x = np.linspace(-10,10,500)
# y = m*x + b Recta Pendiente/Ordenada al Origen
y1 = 0.5*x + 10
y2 = 6*x - 2
y3 = 10*x + 2
y4 = -4*x + 7
mpl.figure(1)
mpl.title("Representaciones Graficas. Rectas")
mpl.grid()
mpl.plot(x,y1,"s",c="b")
mpl.plot(x,y2,c="r")
mpl.plot(x,y3,c="g")
mpl.plot(x,y4,c="y")

mpl.figure(2)
mpl.title("Representaciones Graficas. Senoidales")
mpl.grid()
for i in x:
    Q1 = math.sin(i)
    Q2 = math.cos(i)
    mpl.figure(2)
    mpl.plot(i,Q1,".",c="g")
    mpl.plot(i,Q2,".",c="r")
