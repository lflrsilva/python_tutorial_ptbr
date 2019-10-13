#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt

# funcao objetivo para custo do tanque
def idealCylindricalTank(Di, *args):
    # passagem de argumentos
    rho  = args[0]
    cost = args[1]
    t    = args[2]
    V    = args[3]

    # calculo da funcao custo
    return cost*rho*t*(np.pi*Di**2/2.0 + 4.0*V/Di)


# inicio do programa
if(__name__ == "__main__"):

    # Definicao dos dados do problema
    rho  = 8.05    # kg/m**3
    cost = 5.0     # $/kg
    t    = 5.0e-2  # m
    V    = 100.0   # m**3

    # definindo uma tupla com todos os argumentos para passagem para a funcao
    fargs = (rho, cost, t, V)

    # vamos ver o comportamento da funcao?
    rd = np.linspace(0, 20, 100)
    plt.plot(rd, idealCylindricalTank(rd, *fargs))
    plt.show()

    # definindo limites de busca
    bds = (0.0, 30.0)

    # aplicando minimizacao
    res = minimize_scalar(idealCylindricalTank, args=fargs, bounds=bds,
                          method='bounded', options={'xatol': 1.0e-8,
                                                     'disp': 3})
    D = res.x

    # analisando L/D
    L = 4.0*V/(np.pi*D**2)
    print("L/D = %5.5e" % (L/D))
