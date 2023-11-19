# Generator expression, Iterables e Iterators em Python
# Generator são funções que sabem pausar
import sys

iterable = ["Eu", "Tenho", "__iter__"]
iterator = iter(iterable)  # iterator entrega somente o próximo valor

l1 = [n for n in range(10000)]  # consegue acessar índices específicos
generator = (
    n for n in range(10000)
)  # como não está na memória, não consegue acessar índices específicos

print(sys.getsizeof(l1))
print(generator)

for n in generator:
    print(n)
