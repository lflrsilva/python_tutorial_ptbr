#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Teste do uso de metodo multivariado em um caso univariado

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
# Minimizacao da funcao usando um metodo de dominio aberto e configuracao padrao
    x0   = 3.0    # estimativa inicial
    res1 = minimize(func1, x0, options={'disp' : True})
    print("Using default parameters")
    print("x = %5.5e" % (res1.x))
    print("f = %5.5e" % (res1.fun))

# Vamos aprimorar usando as funcoes jacobiano e hessiana
# Vamos ainda escolher um metodo mais acurado
    x0   = 3.0    # estimativa inicial
    res2 = minimize(func1, x0, method='CG', jac=jac1, hess=hess1,
                    options={'disp' : True})
    print("Using Conjugate-Gradient method")
    print("x = %5.5e" % (res2.x))
    print("f = %5.5e" % (res2.fun))

# Vamos usar outro metodo como teste
    x0   = 3.0    # estimativa inicial
    res3 = minimize(func1, x0, method='Newton-CG', jac=jac1, hess=hess1,
                    options={'disp' : True})
    print("Using mixed Newton-Conjugate-Gradient method")
    print("x = %5.5e" % (res3.x))
    print("f = %5.5e" % (res3.fun))

