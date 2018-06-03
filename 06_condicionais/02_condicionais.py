#
# Autor: LF Silva
# Data : 02/06/2018
#
# Operadores em condicionais
#
# Sintaxe do condicional:
#
# if( boolean_expression ):
# TAB    comando executados SE a expressao booleana for true
# TAB    comando executados SE a expressao booleana for true
# TAB    ...
#
# Pode-se usar 4 espaços ao invés de TAB. É importante ressaltar que Python
# assume que qualquer valor não-nulo é true e zero é false.
#
# Sintaxe do condicional com else
# if ( bool_expr ):
#     comando(s) executados SE bool_expr for true
# else:
#     comando(s) executados SE a bool_expr for false

a = 10
b = 20
x = 1

if(a < b):
    print("Execução de print")

# Caso só seja executado um comando, o mesmo pode ser colocado após o if
if(b > a): x = x + 10

if(x < 11):
    x = x - 5
else:
    x = x + 5

print("x = %3d" % x)
