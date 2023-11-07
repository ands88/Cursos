# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

import random

number = random.randint(1, 100)


def duplicate(number):
    result1 = number * 2
    print(f"O número {number} duplicado é {result1}")


def triplicate(number):
    result2 = number * 3
    print(f"O número {number} triplicado é {result2}")


def quadruplicate(number):
    result3 = number * 4
    print(f"O número {number} quadruplicado é {result3}")
    ...


print("O número aleatório é", number)
duplicate(number)
triplicate(number)
quadruplicate(number)
