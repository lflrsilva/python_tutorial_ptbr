#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt

# f(x) = x + 2 cos(x) = 0
def func1(x):
    return x + 2 * np.cos(x)

if __name__ == "__main__":
# Minimizacao da funcao usando um metodo de dominio fechado
    res1 = minimize_scalar(func1)
    print("x = %5.5e" % (res1.x))
    print("f = %5.5e" % (res1.fun))

# Mas qual o comportamento dessa funcao?
    xr = np.linspace(-10, 10, 100)
    plt.plot(xr,func1(xr))
    plt.show()

# pelo grafico, percebe-se que a funcao tem varios minimos! O Scipy usou um
# limite padrao para a busca do minimo. Vamos definir nossos limites usando uma
# tupla com os valores inferior e superior e especificando o metodo boundded. O
# metodo bounded usa um metodologia mista entre Brent e secao aurea.
    bds = (0.0, 10.0)

# Por padrao, a tolerancia absoluta para convergencia do metodo bounded esta
# igual a 1.0e-5. Podemos alterar o valor nas opcoes tambem.

# Em conjunto, vamos ativar a opcao para saida de dados em tela sobre a
# convergencia do metodo. As opcoes de disp sao:
#  0 : sem mensagem. 1 : notificacoes apenas quando nao converge.
#  2 : mostra mensagem quando converge tambem. 3 : mostra resultados das
#  iteracoes.

    res2 = minimize_scalar(func1, bounds=bds, method='bounded',
                           options={'xatol': 1.0e-8, 'disp': 3})
    print("x = %5.5e" % (res2.x))
    print("f = %5.5e" % (res2.fun))
