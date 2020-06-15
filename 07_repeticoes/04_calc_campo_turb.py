#
# Autor: LF Silva
# Data : 13/04/2020
#
#  Exemplo de repetições em Python
#
import numpy as np
import matplotlib.pyplot as plt

# Cálculo da velocidade de ataque em turbinas eólicas em coordenadas espaciais fixas. A velocidade com que o ar chega à turbina pode ser representado por um perfil periódico e com instabilidades ramdômicas (aleatórias) em função do tempo. 
#
# v  = vm + rd*vr
# vr = cos(pi*t)
# rd = aleatório[0,1]
#
# em que vm é a velocidade média, t é o tempo, vr é a velocidade periódica e rd é a flutuação randômica causada pela turbulência variando de 0 a 1. A condição postulada é de que a flutuação só seja aplicada quando a contribuição vr for maior que 0.5. Caso contrário, ela assume valor unitário.
#
# 

# no de pontos de análise
npt = 200

# velocidade de corte, m/s
vc = 0.5

# velocidade média, m/s
vm = 2.0

# instantes de tempo, s
tf = 10.0
t  = np.linspace(0.0, tf, npt)

# criando array nulo de velocidade (para armazenar dados)
v = np.zeros(npt)

# velocidade periódica
vr = np.cos(np.pi*t)

for i in range(len(v)):
    if vr[i] > vc:
        rd   = np.random.rand()
        v[i] = vm + rd*vr[i]
    else:
        v[i] = vm + vr[i]

plt.plot(t,v)
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.show()
