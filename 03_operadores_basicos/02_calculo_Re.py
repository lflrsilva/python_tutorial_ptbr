#
# Autor : Luiz Fernando L. R. Silva
# Data  : 31/05/2018
#
# Calculo do numero de Reynolds

# Definição de variáveis
Lref = 2e-2     # comprimento característco (m)
u    = 2.0      # velocidade de referencia (m/s)
mu   = 1e-5     # viscosidade dinâmica (kg/m/s ou kg/(m*s))
rho  = 1e3      # massa específica (kg/m**3)

# Cálculo de Re
Re = rho*u*Lref/mu
print(Re)

# Analise o resultado! Existe um erro de precisão, que é intrínseco a
# qualquer cálculo numérico!
