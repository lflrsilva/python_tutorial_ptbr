#
# Autor: LF Silva
# Data : 13/04/2020
#
# Uso de exceções para análise e avaliação de erros
# Erros possíveis:
# - ValueError : erro relacionado a valores
# - IOError    : erro relacionado a leitura e escrita em arquivos

while True:
    try:
        # caso o usuário entre 
        n = input("Entre com um número: ")
        n = int(n)
        break
    except ValueError:
        print("No. não é um inteiro! Por favor, tente novamente...")
print("Ótimo, você inseriu um no inteiro!")
