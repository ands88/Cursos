# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

import copy

# Aumenta os preços em 10%

novos_produtos = []
for produto in produtos:
    novo_produto = copy.deepcopy(produto)
    novo_produto['preco'] *= 1.10
    novos_produtos.append(novo_produto)

# Exibe os produtos originais e os novos produtos
print("Produtos Originais:")
for produto in produtos:
    print(f"{produto['nome']}: R${produto['preco']:.2f}")

print("\nNovos Produtos:")
for produto in novos_produtos:
    print(f"{produto['nome']}: R${produto['preco']:.2f}")

print()

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordena os produtos por nome em ordem decrescente na lista original
produtos.sort(key=lambda x: x['nome'], reverse=True)

# Gera uma cópia profunda dos produtos ordenados
produtos_ordenados_copia = copy.deepcopy(produtos)

# Exibe os produtos originalmente ordenados e a cópia profunda
print("Produtos Originalmente Ordenados por Nome (Decrescente):")
for produto in produtos:
    print(f"{produto['nome']}: R${produto['preco']:.2f}")

print()
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos.sort(key=lambda x: x['preco'])

# Gera uma cópia profunda dos produtos ordenados
produtos_ordenados_por_preco = copy.deepcopy(produtos)

# Exibe os produtos originalmente ordenados e a cópia profunda
print("Produtos Originalmente Ordenados por Nome (Decrescente):")
for produto in produtos:
    print(f"{produto['nome']}: R${produto['preco']:.2f}")