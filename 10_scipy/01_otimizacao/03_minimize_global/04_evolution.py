#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import differential_evolution

# funcao a ser minimizada
def ackley(x):
    arg1 = -0.2 * np.sqrt(0.5 * (x[0] ** 2 + x[1] ** 2))
    arg2 = 0.5 * (np.cos(2. * np.pi * x[0]) + np.cos(2. * np.pi * x[1]))
    return -20. * np.exp(arg1) - np.exp(arg2) + 20. + np.e

if __name__ == "__main__":
    # definindo limites
    bounds = [(-5, 5), (-5, 5)]

    # workers = no. de processadores para uso (computação paralela!)
    # deve-se usar uma metodologia de atualização deferred para habilitar o
    # paralelismo
    #  res = differential_evolution(ackley, bounds)
    res = differential_evolution(ackley, bounds, updating='deferred',
                                 workers=2)
    print(res)
