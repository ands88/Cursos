# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
""" person = {
    "nome": "Anderson",
    "sobrenome": "Martins",
    "idade": 35,
    "altura": 1.82,
    "endereços": [
        {"rua": "tal tal", "número": 123},
        {"rua": "outra rua", "número": 321},
    ],
}

# print(person, type(person))
print(f"altura: ", person["altura"])

for key in person:
    print(key, person[key]) """


# Manipulando chaves e valores em dicionários

person = {}

key = "nome"
person[key] = "Anderson"
person["sobrenome"] = "Martins"

print(person[key])

person[key] = "Neuber"

print(person[key])

del person["sobrenome"]

print(person)
print(person["nome"])

if person.get("sobrenome") is None:
    print("O sobrenome não existe")
else:
    print(person["sobrenome"])
