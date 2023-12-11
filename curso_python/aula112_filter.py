#filter é um filtro funcional

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

def filter_price(product):
    return product['preco'] >100

#new_products = [ p for p in products if p['preco'] > 10]
new_products = filter(
    #lambda product: product ['preco']>10, 
    filter_price, 
    products)

print_iter(products)
print_iter(new_products)