#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt

# Area superficial topo + fundo
def Atf(D):
    #  Ain2 =
    return 2.32*D**2

# espessura do tanque
def t(D):
    # correlacao em ft (conversao)
    Dft = 3.28084*D
    # espessura em in
    tin = 0.0108*Dft + 0.125

    # retorno em m (conversao)
    return tin/39.37008

# comprimento do tanque
def L(D):
    return 4.0*V/(np.pi*D**2) - D/3.0

# funcao objetivo para custo do tanque
def realCylindricalTank(Di, *args):
    # passagem de argumentos
    rho  = args[0]
    cost = args[1]
    addc = args[2]
    V    = args[3]

    # calculo da funcao custo
    #  return cost*rho*t(Di)*(np.pi*Di*L(Di) + (1.0 + addc)*Atf(Di))
    return 0.0432*V + 0.5*V/Di + 0.3041*Di**2 + 0.0263*Di**3

# inicio do programa
if(__name__ == "__main__"):

    # Definicao dos dados do problema
    rho  = 8.05    # kg/m**3
    cost = 5.0     # $/kg
    addc = 0.5     # (-)
    #  V    = 9085.0  # m**3
    V    = 2500    # gal

    # definindo uma tupla com todos os argumentos para passagem para a funcao
    fargs = (rho, cost, addc, V)

    # vamos ver o comportamento da funcao?
    rd = np.linspace(0, 60, 100)
    plt.plot(rd, realCylindricalTank(rd, *fargs))
    plt.show()

    # definindo limites de busca
    bds = (0.0, 60.0)

    # aplicando minimizacao
    res = minimize_scalar(realCylindricalTank, args=fargs, bounds=bds,
                          method='bounded', options={'xatol': 1.0e-8,
                                                     'disp': 3})
    D = res.x

    # analisando L/D
    print("L/D = %5.5e" % (L(D)/D))
