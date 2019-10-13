#
# Autor: LF Silva
# Data  : 12/10/2019
#
#  Introdução ao uso de Numpy - Visualizando resultados
import numpy as np
import matplotlib.pyplot as plt

# comando meshgrid é usado para arranjar arrays 2D em uma malha retangular para
# valores de x e y. A partir de dois arrays 1D (pontos da malha), obtém-se dois
# arrays 2D com todos os pares (x,y). Com estes, é possível visualizar os
# resultados

# criar pontos da malha
points = np.arange(-5, 5, 0.01)

# criar a malha
xs, ys = np.meshgrid(points, points)

# resultado a ser visualizado com base nos pontos
z = np.sqrt(xs ** 2 + ys ** 2)

plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.show()
