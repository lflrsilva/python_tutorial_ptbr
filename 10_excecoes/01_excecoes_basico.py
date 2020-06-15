#
# Autor: LF Silva
# Data : 13/04/2020
#
# Uso de exceções para análise e avaliação de erros

# Existem situações onde sabe-se, a priori, que o código pode falhar de acordo
# com uma exceção específica. Imagine que você montou todo o seu código e tentou
# se cercar de todas as possibilidades para a execução. Contudo, existe um caso
# em que ele pode falhar sendo, portanto, uma exceção. Um exemplo disso é a
# divisão por zero ou a leitura de um arquivo que não existe.

# Vamos analisar os comandos abaixo
#
# >>> n = int(input("Entre com um número: "))
# >>> Entre com um número: 23.5
#  Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
#  ValueError: invalid literal for int() with base 10: '23.5'
#
# O código em si não restringiu o tipo de variável (no caso, um inteiro). E se o
# usuário insere um ponto flutuante? Ou escreve por extenso como uma string?

# Vamos usar a exceção
while True:
    try:
        n = input("Entre com um número: ")
        n = int(n)
        break
    except ValueError:
        print("No. não é um inteiro! Por favor, tente novamente...")
print("Ótimo, você inseriu um no inteiro!")

# Caso o script acuse um erro ao tentar converter o valor da variável para
# o tipo inteiro, pode-se usar a exceção para tentar novamente. Portanto, 
# evita-se a interrupção na execução do script. 
