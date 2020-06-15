#
# Autor : Luiz Fernando L. R. Silva
# Data  : 13/04/2020
#
# Cálculo do coeficiente de difusão para gases
# usando a correlação de Fuller, Schettler e Giddings
# obtida em [1].
#
# Os dados da correlação são:
#
# - Dab : coeficiente de difusão em cm**2/s
# - T   : temperatura em K
# - p   : pressão absoluta em atm
# - Ma  : massa molecular da espécie A (kg/kgmol)
# - Mb  : massa molecular da espécie B (kg/kmol)
# - SVa : volume atômico para difusão para a espécie A (*)
# - SVb : volume atômico para difusão para a espécie B (*)
#
# (*) Valores podem ser obtidos na Tab. 24.3 de [1]
#
# Referências:
# [1] Welty, J. R., Wicks, C. E., Wilson, R. E., Rorrer, G. L., "Fundamentals
#     of Momentum, Heat, and Mass Transfer", John Wiley & Sons, 5a ed., 2008
import numpy as np
import matplotlib.pyplot as plt

# Definição das variáveis
p = 1.0      # em atm

# Intevalo de temperatura
Tinf = float(input("Entre com o limite inferior de temperatura analisado (K): "))
Tsup = float(input("Entre com o limite superior de temperatura analisado (K): "))
T = np.arange(Tinf,Tsup, 5)

# Definição das variáveis das espécies envolvidas
# Avaliando CO2 em Ar
Ma = 44.0
Mb = 28.8
SVa = 26.9
SVb = 20.1

# Cálculo da corelação
# função pow calcula expoente de forma eficiente
SV  = np.power(SVa, 1.0/3.0) + np.power(SVb, 1.0/3.0)
# função sqrt calcula raiz quadrada de forma eficiente
MM  = np.sqrt(1.0/Ma + 1.0/Mb)

Dab = 1.0e-3*np.power(T,1.75)*MM/(p*SV**2)

# impressão em tela
np.set_printoptions(precision=3)
print(f"Dab = {Dab} cm**2/s")

# Construção de gráfico para análise
# Criando elemento de plot
plt.plot(T, Dab)
# Configurando eixos
plt.xlabel("T (K)")
plt.ylabel("Dab (cm**2/s)")
# mostrando em tela
plt.show()
