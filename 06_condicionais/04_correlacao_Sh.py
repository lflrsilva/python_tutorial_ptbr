#
# Autor: LF Silva
# Data : 02/06/2018
#
# Correlação para convecção forçada em placa plana
import math as m

# propriedades físicas e mássicas
nu  = 1.5e-5         # viscosidade cinemática, m**2/s
Dab = 1.3e-6         # difusividade mássica, m**/s

# Característica geométrica
L = 2.0              # comprimento da placa, m

# Característica do escoamento
v = 1.2              # velocidade incidente, m/s

# Cálculo dos adimensionais
Re = v*L/nu
Sc = nu/Dab

# Cálculo de Sherwood
if(Re < 2.0e5):
    # caso laminar
    Sh = 0.664*m.sqrt(Re)*m.pow(Sc, 1.0/3.0)
else:
    # caso turbulento
    Sh = 0.0365*m.pow(Re,0.8)*m.pow(Sc, 1.0/3.0)

print("Sh = %5.5f" % Sh)

# obtendo o coeficiente de convecção mássico
hm = Sh*Dab/L
print("hm = %5.5f kg/s" % hm)
