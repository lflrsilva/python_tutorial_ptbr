#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import dual_annealing
import matplotlib.pyplot as plt

# funcao a ser minimizada
def rastrigin(x):
    return np.sum(x*x - 10*np.cos(2*np.pi*x)) + 10*np.size(x)

if __name__ == "__main__":
    # definindo limites em um sistema com 10 valores
    lw = [-5.12] * 10
    up = [5.12] * 10
    # check para ver como funciona
    print(lw)

    # seed = referência para inicialização aleatória da estimativa inicial
    # se uar a mesma semente, a sequência de números aleatórios é a mesma!
    res = dual_annealing(rastrigin, bounds=list(zip(lw, up)), seed=1234)
    print(res)
