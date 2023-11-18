# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.


# print(list(range(10)))
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


l1 = []
for number in range(10):
    l1.append(number)

# print(l1)

l2 = [number * 2 for number in range(10)]
# print(l2)


# mapeamento de datos em list comprehension

products = [
    {"nome": "p1", "preço": 20},
    {"nome": "p2", "preço": 10},
    {"nome": "p3", "preço": 30},
    {"nome": "p4", "preço": 50},
]

new_products = [
    {**products, "preço": products["preço"] * 1.05}
    if products["preço"] > 20
    else {**products}  # if ternário
    for products in products
    if (products["preço"] >= 20 and products["preço"] * 1.05) > 10
]

p(new_products)

lista = [n for n in range(10) if n < 5 and n > 2]
print(lista)
