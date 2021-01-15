import matplotlib.pyplot as mpl
import numpy as np
from skimage import io
from skimage.color import rgb2gray
mpl.close("all")

Ima1 = io.imread('placa.jpg')
mpl.figure(1)
mpl.subplot(2,2,1)
mpl.title("Imagen en RGB")
mpl.imshow(Ima1)

gris = rgb2gray(Ima1)
mpl.subplot(2,2,2)
mpl.title("Imagen en Escala de Grises")
mpl.imshow(gris,cmap="gray")

binario = gris<0.3
mpl.subplot(2,2,3)
mpl.title("Imagen Binarizada al 30%")
mpl.imshow(binario, cmap="gray")

recorte = binario[85:235,35:660]
mpl.subplot(2,2,4)
mpl.title("Placa Recortada")
mpl.imshow(recorte,cmap="gray")

sumacol = np.sum(recorte, axis=0) #axis=0 Columnas
mpl.figure(2)
mpl.plot(sumacol)

