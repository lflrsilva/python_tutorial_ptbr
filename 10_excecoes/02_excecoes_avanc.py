"""
 Autor: LF Silva
 Data : 13/04/2020

 Ainda é possível criar modos de avaliação de erros em blocos

    try:
        tenta esse comando
    except:
        se der algum erro, tente esse comando

 Mais informações:
 https://realpython.com/python-exceptions/
 https://docs.python.org/3/library/exceptions.html
 https://dbader.org/blog/python-assert-tutorial
"""
import sys


# vamos montar uma função simples de avaliação de sistema operacional
def linux_int():
    assert("linux" in sys.platform), "Mano, já te disse que só roda em Linux"


if __name__ == '__main__':
    # INÍCIO COMENTÁRIO 1
    # try:
    #     linux_int()
    # except:
    #     print("Função exclusiva para linux não foi executada.")
    # FIM COMENTÁRIO 1

    # mas não foi possível ver a sua mensagem customisada de erro
    # INÍCIO COMENTÁRIO 2
    # try:
    #     linux_int()
    # except AssertionError as linux_erro:
    #     print(linux_erro)
    #     print("Função exclusiva para linux não foi executada.")
    # FIM COMENTÁRIO 2

    # Existem vários tipos de erros de exceção. Busque informação
    # no manual do Python para ver as possibilidades.
    # FileNotFoundError é, bem, para tentativa de leitura de
    # arquivos que não foram encontrados.
    # INÍCIO COMENTÁRIO 3
    # try:
    #     with open('file.log') as file:
    #         read_data = file.read()
    # except FileNotFoundError as fnf_erro:
    #     print(fnf_erro)
    # FIM COMENTÁRIO 3

    # E se combinarmos os erros? Funciona?
    # INÍCIO COMENTÁRIO 4
    # try:
    #     linux_int()
    #     with open('file.log') as file:
    #         read_data = file.read()
    # except FileNotFoundError as fnf_erro:
    #     print(fnf_erro)
    # except AssertionError as linux_erro:
    #     print(linux_erro)
    #     print("Função exclusiva para linux não foi executada.")
    # FIM COMENTÁRIO 4

    # Importante!
    # - o bloco try é executado até atingir a primeira exceção.
    # - você pode definir como o script responde à execeção dentro
    #   de except
    # - usar exceções múltiplas pode ficar confuso...

    # Vamos aprender o bloco try: else:
    # INÍCIO COMENTÁRIO 5
    try:
        linux_int()
    except AssertionError as linux_erro:
        print(linux_erro)
        print("Função exclusiva para linux não foi executada.")
    else:
        try:
            with open('file.log') as file:
                read_data = file.read()
        except FileNotFoundError as fnf_erro:
            print(fnf_erro)
    # FIM COMENTÁRIO 5

    # try:
    #    execute comandos
    # except:
    #    execute se encontrar exceções
    # else:
    #    execute se não encontrar exeções
    # finally:
    #    execute de qualquer maneira
