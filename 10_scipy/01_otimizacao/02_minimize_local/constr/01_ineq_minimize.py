#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import minimize, Bounds
import matplotlib.pyplot as plt

# Teste de minimização com restrições de desigualdade linear

# f(x) = x + 2 cos(x) = 0
def func1(x):
    return x + 2 * np.cos(x)

# Jacobiano (1a derivada)
def jac1(x):
    return 1.0 - 2*np.sin(x)

# Hessiana (2a derivada)
def hess1(x):
    return -2*np.cos(x)

if __name__ == "__main__":
    xr = np.linspace(-10, 10, 100)
    plt.plot(xr,func1(xr))
    plt.show()

    # busca por pto de minimo local com base na estimativa inicial
    x0   = -10.0    # estimativa inicial
    res = minimize(func1, x0, method='Newton-CG', jac=jac1, hess=hess1,
                    options={'disp' : True})
    print("Using mixed Newton-Conjugate-Gradient method")
    print("x = %5.5e" % (res.x))
    print("f = %5.5e" % (res.fun))

    # criando restricoes de desigualdade linear ( 0 <= x <= 5 )
    # argumentos para as restricoes (lim. inf., lim. sup)
    bds = Bounds(0.0, 5.0)

    # busca por pto de minimo local com base na estimativa inicial
    # e sujeito a restricao de desigualdade linear.
    # Obs.: Apenas os metodos trust-constr, SLSQP e COBYLA podem usar
    # restricoes.
    x0   = np.array([-10.0])    # estimativa inicial DEVE ser um ndarray !!
    res1 = minimize(func1, x0, method='SLSQP', jac=jac1, hess=hess1,
                    bounds=bds, options={'disp' : True})
    print("Using SLSQP method with inequality limit restrictions")
    print("x = %5.5e" % (res1.x))
    print("f = %5.5e" % (res1.fun))
