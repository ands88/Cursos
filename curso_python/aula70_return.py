"""
Retorno de valores das funções (return)
"""


def soma(x, y):
    if x > 10:
        return "Parou por aqui"
    return (
        x + y
    )  # o return diz para o python parar tudo e retornar essa função, acabando a execução dela


# variavel = soma (1, 2)
# variavel = int ('1')

soma1 = soma(2, 2)
soma2 = soma(3, 3)

print(soma1, "e", soma2)
print(soma1 + soma2)
print(soma(11, 55))
