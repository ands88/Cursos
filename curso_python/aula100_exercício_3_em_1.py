# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

import copy 

# Aumenta os preços em 10%
new_products = []
for item in products:
    new_products = copy.deepcopy(item)
    new_products['preco'] *= 1.10
    new_prooducts.append(new_products)

# lista dos produtos com os valores originais e modificados

print("Produtos:")
for item in products:
    print(f"{item['nome']}: R${item['preco']:.2f}")
print()

print("Novos Preços:")
for item in new_products:
    print(f"{item['nome']}: R${item['preco']:.2f}")


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

new_products = []
for item in products:
    new_products = copy.deepcopy(item)
    new_products = append(new_products)
new_products = sorted(new_products, key=lambda item: item["nome"])

print(new_products)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)