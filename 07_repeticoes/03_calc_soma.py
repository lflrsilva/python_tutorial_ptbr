#
# Autor: LF Silva
# Data : 13/04/2020
#
#  Exemplo de repetições em Python
#
import numpy as np

# Calculo da energia cinética total de um grupo de 10 partículas
# Ec = sum_i 1/2 m_i v_i*v_i, em que i = 1,2...,10

# definição de variáveis
# massa das partículas (kg)
m = np.array([0.50, 0.30, 0.70, 0.40, 0.01,
              0.87, 0.55, 0.33, 0.27, 1.80])
# velocidade das partículas (m/s)
v = np.array([1.05, 0.40, 3.40, 1.44, 9.03,
              2.74, 3.25, 2.53, 4.37, 0.50])

# calculo da energia cinética - método 1
Ec = 0.0
for i in range(len(m)):
    Ec += m[i]*v[i]*v[i]
Ec *= 0.5
print(f"A energia cinética total é {Ec:5.5f} J")

# calculo da energia cinética - método 2
# Usando recursos Numpy
Ec = 0.0
for mi,vi in np.nditer([m,v]):
    Ec += mi*vi*vi
Ec *= 0.5
print(f"A energia cinética total é {Ec:5.5f} J")

# calculo da energia cinética - método 3
# Usando recursos Numpy
Ec = 0.5*np.sum(m*v*v)
print(f"A energia cinética total é {Ec:5.5f} J")
