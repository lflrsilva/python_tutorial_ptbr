#
# Autor : LF Silva
# Data  : 03/06/2018
#
# Difusão transiente - Cap. 27, ex. 2, Welty et al, 5a ed.
#
# Liberação de droga no organismo ao longo do tempo. São dados:
#
# - ma0 : massa inicial de droga, mg
# - Dab : coeficiente de difusão, cm**2/s
# - ca0 : concentração inicial da droga, mg/cm**3
# - cas : concentração da droga na superfície do comprimido, mg/cm**3
# - R   : raio do comprimido esférico, cm
import math as m
import numpy as np
import matplotlib.pyplot as plt

# Definindo variáveis
ma0 = 10.00    # mg
ca0 = 68.90    # mg/cm**3
cas = 0.000    # mg/cm**3
Dab = 3.0e-7   # cm**2/s
R   = 0.326    # cm

## variáveis numéricas
# avaliação ao longo do raio
nr = 25
R0 = 0.0                    # centro da esfera
r  = np.linspace(R0, R, nr)
c  = np.empty(nr)           # concentração adimensional ao longo do raio

# avaliação ao longo do tempo
nt = 20
t0 = 0.0
tf = 21.6e3    # == 6.0 h
# tf = 24*3600.0    # == 24.0 h
t  = np.linspace(t0, tf, nt)
ma = np.empty(nt)           # massa adimensional ao longo do tempo

# variáveis auxiliares para cálculo de termos do somatório
tol = 1.0e-16     # tolerância para somatório
nsum_max = 100    # número máximo de termos no somatório

print("t \t 1-ma/ma0")

# organizando informações para o gráfico
plt.subplot(2, 1, 1)
plt.grid()

# nomes dos eixos
plt.xlabel("r (cm)")
plt.ylabel("c (mg/cm**3)")

# limites dos eixos
plt.ylim(0.0, 70.0)
plt.xlim(R0, 0.35)

for it in range(nt):
    if (it == 0 ):
        # primeiro instante de tempo
        # aplicando condição inicial
        c[:]   = ca0      # c  = ca0 para todo raio, uso de [:] para aplicar
                          # o valor a todos os elementos do array.

        # armazenando curva no gráfico
        lbl = (f"t = {t[it]/3600.0:.2f}")
        plt.plot(r, c, label=lbl)

        ma[it] = 1.0      # ma = ma0/ma0
        print(f"{t[it]/3600.0:5.3f} \t {1-ma[it]:5.3f}")
        continue

    for ir in range(nr):
        Fo = Dab*t[it]*(np.pi/R)**2   # variável auxiliar
        if(ir == 0):
            # condição especial para centro da esfera, Eq. 27.20
            soma = 0.0
            for n in range(nsum_max):
                nn = n + 1            # contador do somatório inicia em 1
                somar = m.pow(-1, nn) \
                      * np.exp(-Fo*nn*nn)

                if (np.fabs(somar) < tol):
                    # tolerancia para o somatório foi atingida!
                    #  print("iterações em r = %f : %d" % (r[ir], n))
                    break
                # atualiza valor do somatório
                soma += somar

            Y     = 1.0 + 2.0*soma
            c[ir] = ca0 + Y*(cas - ca0)

        else:
            # condição para outros raios, Eq. 27,19
            soma = 0.0
            Ro   = np.pi*r[ir]/R      # variável auxiliar
            for n in range(nsum_max):
                nn = n + 1            # contador do somatório inicia em 1
                somar = (m.pow(-1, nn)/nn) \
                      * np.sin(Ro*nn) \
                      * np.exp(-Fo*nn*nn)

                if (np.fabs(somar - soma) < tol):
                    # tolerancia para o somatório foi atingida!
                    #  print("iterações em r = %f : %d" % (r[ir], n))
                    break
                # atualiza valor do somatório
                soma += somar

            Y     = 1.0 + (2.0*R/np.pi/r[ir])*soma
            c[ir] = ca0 + Y*(cas - ca0)

    # armazenando curva ca no gráfico
    lbl = (f"t = {t[it]/3600.:0.2f}")
    plt.plot(r, c, label=lbl)
    #  plt.legend()

    # cálculo da massa adimensional total para t[it]
    soma = 0.0
    for n in range(nsum_max):
        nn = n + 1            # contador do somatório inicia em 1
        somar = np.exp(-Fo*nn*nn)/nn/nn

        if (np.fabs(somar - soma) < tol):
            # tolerancia para o somatório foi atingida!
            #  print("iterações em t = %3.4f : %d" % (t[it], n))
            break

        # atualiza valor do somatório
        soma += somar

    ma[it] = 6.0*soma/np.pi/np.pi
    print(f"{t[it]/3600.0:5.3f} \t {1.0 - ma[it]:5.3f}")
    # convertendo o tempo para horas


# armazenando curva para ma/ma0
plt.subplot(2, 1, 2)
plt.plot((t/3600.0),1-ma)    # convertendo o tempo para horas
plt.grid()

# nome dos eixos
plt.xlabel("t (h)")
plt.ylabel("1 - ma/ma0 (-)")

# limites dos eixos
plt.ylim(0.0, 1.0)
plt.xlim(0.0, tf/3600.0)

plt.show()
