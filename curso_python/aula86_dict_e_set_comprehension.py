# Dictionary comprehension e set comprehension

product = {
    "nome": "Caneta Azul",
    "preço": 2.5,
    "categoria": "Escritório",
}

# print(product.items())

new_dict = {
    chave: valor.upper() if isinstance(valor, (str)) else valor
    for chave, valor in product.items()
    if chave != "categoria"
}
print(new_dict)
print()

l1 = [
    ("a", "valor a"),
    ("b", "valor b"),
    ("c", "valor a"),
]
dc = {chave: valor for chave, valor in l1}

print(dc)
print()

s1 = {i**2 for i in range(10)}
print(s1)
