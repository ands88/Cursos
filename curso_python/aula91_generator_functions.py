# Introdução às Generator functions em Python

# generator = (n for n in range(1000000))

""" 
def generator(n=0):
    yield 1  # pausa
    print("Continuando...")
    yield 2
    print("Continuando...")
    yield 3
    print("Terminar")
    return "ACABOU" """


""" test = generator(n=0)

for n in generator(n=0):
    print(n) """


# print(next(test))
# print(next(test))


def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n >= maximum:
            return


test = generator(maximum=2500)

for n in test:
    print(n)
