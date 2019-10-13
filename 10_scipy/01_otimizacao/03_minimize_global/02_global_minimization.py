#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import shgo, dual_annealing, differential_evolution, basinhopping
import matplotlib.pyplot as plt

# funcao a ser minimizada
def eggholder(x):
    return (-(x[1] + 47) * np.sin(np.sqrt(abs(x[0]/2 + (x[1]  + 47))))
            -x[0] * np.sin(np.sqrt(abs(x[0] - (x[1]  + 47)))))

if __name__ == "__main__":
    # limites de análise
    bounds = [(-512, 512), (-512, 512)]

    results = dict()

    results['shgo'] = shgo(eggholder, bounds)
    print(results['shgo'])


    results['da'] = dual_annealing(eggholder, bounds)
    print(results['da'])


    results['de'] = differential_evolution(eggholder, bounds)
    print(results['de'])


    results['bh'] = basinhopping(eggholder, bounds)
    print(results['bh'])


    results['shgo_sobol'] = shgo(eggholder, bounds, n=200, iters=5,
                                 sampling_method='sobol')

    # grafico com resultados por método
    x = np.arange(-512, 513)
    y = np.arange(-512, 513)
    xgrid, ygrid = np.meshgrid(x, y)
    xy = np.stack([xgrid, ygrid])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    im = ax.imshow(eggholder(xy), interpolation='bilinear', origin='lower',
                   cmap='gray')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    def plot_point(res, marker='o', color=None):
        ax.plot(512+res.x[0], 512+res.x[1], marker=marker, color=color, ms=10)

    plot_point(results['bh'], color='y')  # basinhopping           - yellow
    plot_point(results['de'], color='c')  # differential_evolution - cyan
    plot_point(results['da'], color='w')  # dual_annealing.        - white

# SHGO produces multiple minima, plot them all (with a smaller marker size)
    plot_point(results['shgo'], color='r', marker='+')
    plot_point(results['shgo_sobol'], color='r', marker='x')
    for i in range(results['shgo_sobol'].xl.shape[0]):
        ax.plot(512 + results['shgo_sobol'].xl[i, 0],
                512 + results['shgo_sobol'].xl[i, 1],
                'ro', ms=2)

    ax.set_xlim([-4, 514*2])
    ax.set_ylim([-4, 514*2])
    plt.show()
