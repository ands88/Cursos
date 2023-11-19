# try, except, else, finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print("ABRIR O ARQUIVO")
    8 / 2
except (
    ZeroDivisionError
) as error:  # trata a exceção, e pode ter quantos quiser dentro do try
    print("DIVIDIU POR ZERO")
    print(error)
else:  # executado quando não há erro
    print("NÃO DEU ERRO!")
finally:  # não trata a exceção
    print("FECHAR O ARQUIVO")
