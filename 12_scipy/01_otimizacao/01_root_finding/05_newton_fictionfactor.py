#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import newton

# Eq. de Colebrook para fator de atrito
# (Fox & McDonalds, 6ed., p. 340)
def friction_factor(x, *args):
    # recuperando os argumentos
    # a passagem de tupla para funcao deve ter *
    eD = args[0]
    Re = args[1]
    return 1.0/np.sqrt(x) + 2 * np.log10(eD/3.7 + 2.51/Re/np.sqrt(x))

if __name__ == "__main__":
# dados de processo
    eD = 0.0002 # rugosidade relativa
    Re = 3e6    # Reynolds

# Estimativa inicial (Fox & McDonalds, 6ed., p. 341)
    xguess  = 0.25/(np.log10(eD/3.7 + 5.7/Re**0.9))**2

# Passagem de argumentos por tupla
    fargs = (eD, Re)

    xsol = newton(friction_factor, xguess, args=fargs)
    print(f"f_D = {xsol:5.5e}")
    print(f"fun = {friction_factor(xsol,*fargs):5.5e}")
