# reduce - faz a redução de um iterável em um valor
from functools import reduce

products = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

""" def func_reduce(acumulador, produto):
    print(acumulador)
    print('produto', produto)
    print()
    return acumulador + produto ['preco'] """

total = reduce (lambda ac, p: ac+p['preco'], products, 0)

print('O total é', total)

""" total = 0
for p in produtos:
    total += p['preco']

print (total) """