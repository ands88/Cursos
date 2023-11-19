# try, except, else, finally

try:
    print("ABRIR O ARQUIVO")
    8 / 2
except ZeroDivisionError as error:  # trata a exceção
    print("DIVIDIU POR ZERO")
    print(error)
else:  # executado quando não há erro
    print("NÃO DEU ERRO!")
finally:
    print("FECHAR O ARQUIVO")
