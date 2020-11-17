""" Autor: LF Silva
 Data : 13/04/2020
        17/11/2020

 Uso de exceções para análise e avaliação de erros

 Para pensar: Se você estiver na beira de um precipício e sabe que
 precisa pular. Você prefere pular logo ou é melhor olhar antes,
 perceber que é alto e usar um paraquedas?

 Um script em Python pode interromper sua execução por dois motivos: erro
 na sintaxe ou por exceção. Mas qual a diferença?

 - erro de sintaxe:

 >>> print(0/0))
 File "<stdin>", line 1
    print( 0 / 0 ))
                  ^
 SyntaxError: invalid syntax

 - erro de execeção:

 >>> print(0/0)
 Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
 ZeroDivisionError: integer division or modulo by zero

 Portanto, existem situações onde sabe-se, a priori, que o código pode falhar
 de acordo com uma exceção específica. Imagine que você montou todo o seu
 código e tentou se cercar de todas as possibilidades para a execução. Contudo,
 existe um caso em que ele pode falhar sendo, portanto, uma exceção. Um exemplo
 disso é a divisão por zero ou a leitura de um arquivo que não existe.

 Nessa condição, o script é interrompido pelo erro. Mas e se existisse uma
 forma de avaliar se erro existe e dar uma segunda chance usando outra
 estratégia? Essa é uma vantagem do uso de exceções.

 Além disso, muitas vezes as mensagens de erro não apresentam mensagem de erro
 muito explicativas. Por isso, o desenvolvedor pode lançar (raise) uma
 mensagem, um aviso customizado. Essa é outra vantagem no uso de excecões.
"""
import sys

# Teste 1
# digamos que, por uma acaso da vida, o seu resultado deu 8. Você pode avaliar
# se o mesmo é consistente e lançar (raise) uma mensagem caso não seja.
# O comando Exception interrompe a execução do script e informa a mensagem com
# classificação Exception.
# INICIO COMENTARIO 1
x = 8
if(x > 5):
    raise Exception(f"x não pode exceder 5. O valor obtido foi {x}")

# FIM COMENTARIO 1

# Se se formos assertivos em relação a um possível erro e já se precaver
# de determinada situação. Para o comando assert:
# Se a condição for True, o script continua
# Se a condição for False, o script lança o AssertionError
# INICIO COMENTARIO 2
# assert('linux' in sys.platform), \
#     "Esse programa só pode ser executado em Linux!"

# FIM COMENTARIO 2
