# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicacao1 = multiplicacao(1, 2, 3)
print(multiplicacao1)

multiplicacao2 = multiplicacao(4, 5, 6)
print(multiplicacao2)

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 100
multiplicacao3 = multiplicacao(*numeros)
print(multiplicacao3)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def checagem(x):
    modulo = x % 2
    if modulo == 0:
        print(f"{x} é par.")
    else:
        print(f"{x} é impar.")


checagem(777)
