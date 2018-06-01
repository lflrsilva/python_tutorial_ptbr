#
# Autor : Luiz Fernando L. R. Silva
# Data  : 31/05/2018
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

# Definição das variáveis termodinâmicas
T = 293.15   # em K
p = 1.0      # em atm

# Definição das variáveis das espécies envolvidas
# Avaliando CO2 em Ar
Ma = 44.0
Mb = 28.8
SVa = 26.9
SVb = 20.1

# Cálculo da corelação
SV  = SVa**(1.0/3.0) + SVb**(1.0/3.0)
MM  = (1.0/Ma + 1.0/Mb)**(0.5)

Dab = 1.0e-3*(T**1.75)*MM/(p*SV**2)
print("Dab = ", Dab, "cm**2/s")
