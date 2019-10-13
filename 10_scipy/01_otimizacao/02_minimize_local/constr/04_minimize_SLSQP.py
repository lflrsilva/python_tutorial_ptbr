#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import minimize, Bounds

# Teste de minimização com múltiplas restrições
# min f(x_0, x_1) = 100.0*(x_1 - x_0*x_0)**2 + (1 - x_0)**2
# com restrições
# x_0 + 2*x_1  <= 1.0
# x_0**2 + x_1 <= 1.0
# x_0**2 - x_1 <= 1.0
# 2*x_0 + x_1 = 1.0
# e limites
# 0.0  <= x_0 <= 1.0
# -0.5 <= x_1 <= 2.0
#
# Resposta: x_0 = 0.4149, x_1 = 0.1701

# função objetivo
def fa(x):
    return(100*(x[1]-x[0]**2)**2 + (1.0-x[0])**2)

# restrições de igualdade
# 2*x_0 + x_1 = 1.0    -> 2*x_0 + x_1 - 1 = 0
def eq_cons(x):
    return np.array( [2.0*x[0] + x[1] - 1.0] )

# jacobiano das restrições de igualdade
def eq_J(x):
    return np.array([[2.0, 1.0]])

# restrições de desigualdade
# x_0 + 2*x_1  <= 1.0  -> -x_0 -2*x_1 + 1.0 >= 0
# x_0**2 + x_1 <= 1.0  -> -x_0**2 - x_1 + 1.0 >= 0.0
# x_0**2 - x_1 <= 1.0  -> -x_0**2 + x_1 + 1.0 >= 0.0
def ineq_cons(x):
    return np.array([-x[0] - 2.0*x[1] + 1.0,
                     -x[0]**2 - x[1] + 1.0,
                     -x[0]**2 + x[1] + 1.0])

# jacobiano das restrições de desigualdade
def ineq_J(x):
    return np.array([[-1.0, -2.0],
                     [-2.0*x[0], -1.0],
                     [-2.0*x[0], 1.0]])

if __name__ == "__main__":

    # definindo limites para otimização
    lbnd = [0.0,  -0.5]
    ubnd = [1.0, 2.0]
    bnds = Bounds(lbnd, ubnd)

    # definindo as restrições (dictionary)
    eq_constr  = {'type': 'eq', 'fun': eq_cons, 'jac': eq_J}
    neq_constr = {'type': 'ineq', 'fun': ineq_cons, 'jac': ineq_J}

    # minimizacao usando SLSQP
    x0 = np.array([0.5, 0.0])
    res = minimize(fa, x0, method='SLSQP', constraints=[eq_constr, neq_constr],
                   options={'disp' : True}, bounds=bnds)
    print("x_0 = %5.5e" % (res.x[0]))
    print("x_1 = %5.5e" % (res.x[1]))
    print("f = %5.5e" % (res.fun))
    #  print(res)
