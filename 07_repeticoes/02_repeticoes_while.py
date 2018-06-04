#
# Autor: LF Silva
# Data : 02/06/2018
#
#  Laços e repetições em Python
#
#  Sintaxe basica:
#
#  while ( expression ):
#  TAB    statement1
#  TAB    statement2
#         ...
#
#  Nesta sintaxe, a execução dos comandos são repetidos enquanto 'expression'
#  fornecer a condição true. Para tal, é recomendado que os comandos dentro
#  do laço alterem a condição de 'expresion' senão a repetição será infinita.
#
#  É possível definir uma região de comandos a serem executados quando
#  'expression' for false.
#
#  while ( expression ):
#  TAB    statement1
#  TAB    statement2
#         ...
#  else:
#  TAB    statment3
#  TAB    statment4
#         ...
#

count = 0
maxcount = 10
print("Vamos contar até %d" % maxcount)

while(count < maxcount):
    count += 1          # equivalente a count = count + 1
    print("%d" % count)


