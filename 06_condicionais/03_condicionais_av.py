#
# Autor: LF Silva
# Data : 02/06/2018
#        11/11/2020
#
x = 5

if(x < 6):
    print("Entrei no condicional 1?")
    x = 7

input(f"Valor de x = {x:d}. \nAperte uma tecla para continuar.")

if(x == 0):
    print("Entrei no condicional 2?")
    x = 0

input(f"Valor de x = {x:d}. \nAperte uma tecla para continuar.")

if(0): x = 17

input(f"Valor de x = {x:d}. \nAperte uma tecla para continuar.")

if(1): x = 20

input(f"Valor de x = {x:d}. \nAperte uma tecla para continuar.")

x = 6
if(3 < x < 9):
    print("Olá!")

input(f"Valor de x = {x:d}. \nAperte uma tecla para continuar.")

x = 6
if(9 > x > 3):
    print("Oi!")

input(f"Valor de x = {x:d}. \nAperte uma tecla para continuar.")

# regra de ouro: Nunca use operadores de comparação compartilhados.
#                SEMPRE USE operadores de relação (and / or)!