#
# Autor : LF Silva
# Data  : 14/04/2020
#
# Entrada e saída de dados em arquivo usando Numpy
import numpy as np

# criação de arrays
x = np.arange(10)
z = np.arange(10,20)

# escrevendo em arquivo
np.savetxt("np_data.txt", x)

# E se quisermos mais de um array? Verifique se ficou bom. Consegue melhorar?
np.savetxt("np_dataxz.txt", [x, z])

# lendo o arquivo e armazenado os dados
y = np.loadtxt("np_data.txt")
print(y)
