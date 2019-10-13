#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import minimize

# Teste de minimização bivariado
# f(D,L) = pi*D*L + pi*D*D/4 + pi*D*D/4
# com restrição
# D >= 0.0
# H >= 0.0
# V = (pi*D*D/4)*L
#
# Resposta:  D = 5.03, L = 5.03

# f(D,L) = pi*D*(L + D/4)
def fa(x, *args):
    return(np.pi*x[0]*(x[1] + x[0]/2.0))

# restrição: h(D,L) = (pi*D*D*L)/4 - V = 0
def ha(x, *args):
    return(np.pi*x[0]*x[0]*x[1]/4.0 - args)

if __name__ == "__main__":

    # definindo variaveis
    V = 100.0   # m**3

    # passagem de parâmetros (tupla)
    # declaração de tupla com elemento único
    fargs = (V,)

    # definindo as restrições (dictionary)
    eq_cons = {'type': 'eq', 'fun': ha, 'args': fargs}

    # minimizacao usando SLSQP
    x0 = np.array([1.0, 1.0])
    res = minimize(fa, x0, args=fargs, method='SLSQP', constraints=eq_cons,
                   options={'disp' : True})
    print("D = %5.5e" % (res.x[0]))
    print("L = %5.5e" % (res.x[1]))
    print("f = %5.5e" % (res.fun))
    #  print(res)
