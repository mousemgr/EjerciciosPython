import matplotlib.pyplot as mpl
from skimage import io
import random as rd

cartas = ["r01.jpg","r02.jpg","r03.jpg","r04.jpg","r05.jpg",
          "r06.jpg","r07.jpg","r08.jpg","r09.jpg","r10.jpg",
          "r11.jpg","r12.jpg","r13.jpg","r14.jpg","r15.jpg"]

t=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
aleatorios = rd.sample(t,15)

a=0
while (a<15):
    correYseVa = cartas[aleatorios[a]]
    carta = io.imread(correYseVa)
    mpl.imshow(carta)
    mpl.pause(2)
    a = a + 1