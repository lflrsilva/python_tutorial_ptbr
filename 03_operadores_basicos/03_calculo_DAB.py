#
# Autor : Luiz Fernando L. R. Silva
# Data  : 31/05/2018
#

T = 293.15
p = 1.0

# Avaliando CO2 em Ar
Ma = 44.0
Mb = 28.8
SVa = 26.9
SVb = 20.1

Dab = 1.0e-3*T**1.75/p/(SVa**(1.0/3.0) + SVb**(1.0/3.0))**2 \
      *(1.0/Ma + 1.0/Mb)**(0.5)

print(Dab)
