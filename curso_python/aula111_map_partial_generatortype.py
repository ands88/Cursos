# noa - para mapear dados

from functools import partial
from types import GeneratorType


def print_iter (iterator):
    print(*list(iterator), sep='\n')
    print()

products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def rise_percentage (value, percentage):
    return round(value * percentage, 2)

rise_ten_percent = partial(rise_percentage, percentage=1.1)

#new_products = [ {**p, 'preco':rise_ten_percent(p['preco'])} for p in products]

def change_product_prices(product):
    return {**product, 'preco':rise_ten_percent(product['preco'])}

new_products = (list(map(change_product_prices, products)))

print_iter(products)

print(new_products)
print(hasattr(new_products, '__iter__'))
print(hasattr(new_products, '__next__'))
print(isinstance(new_products, GeneratorType))
# print_iter(new_products)
print(list(map(lambda x:x*3,[1, 2, 3, 4, 5])))