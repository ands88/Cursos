"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

texto = "Anderson"
iterador = iter(texto)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break


# texto = iter("Anderson")  # mesma coisa do __iter__()

# print(next(texto))  # mesma coisa do __next__()


# numeros = range(0, 100, 8)

# for numero in numeros:
#    print(numeros)
