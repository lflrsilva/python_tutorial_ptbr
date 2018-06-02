#
# Autor : LF Silva
# Data  : 01/05/2018
#
# Usando módulo Matplotlib

import numpy as np
import matplotlib.pyplot as plt    # modulo de gráficos simples

# criando array Numpy
x = np.linspace(0, 2, 100)

# primeira curva
plt.plot(x, x, label='linear')
# segunda curva
plt.plot(x, x**2, label='quadratico')
# terceira curva
plt.plot(x, x**3, label='cubico')

# Nome dos eixos
plt.xlabel('x label')
plt.ylabel('y label')

# título do gráfico
plt.title("Plot simples")

# Inserindo legenda
plt.legend()

# mostrando o gráfico
plt.show()

## Podemos criar gráficos conjuntos também
# Vamos criar as curvas
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

# O subplot(ni,nj,N) divide uma janela em ni linhas e nj colunas, referente ao
# gráfico N.
plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')      # o- refere-se ao tipo de linha
plt.title('2 subplots')
plt.ylabel('Oscilação suavizada')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')      # .- refere-se ao tipo de linha
plt.xlabel('tempo (s)')
plt.ylabel('Sem suavização')

plt.show()

# Vários outros tipos de gráficos são possíveis. Para mais informações, veja
# a documentação. Para outros exemplos, veja o link:
#  https://matplotlib.org/tutorials/introductory/sample_plots.html#sphx-glr-tutorials-introductory-sample-plots-py
