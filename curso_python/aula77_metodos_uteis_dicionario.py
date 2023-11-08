# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

dict1 = {
    "nome": "Anderson",
    "sobrenome": "Martins",
    "lista": [0, 1, 2],
}
dict2 = copy.deepcopy(dict1)

dict2["nome"] = "Neuber"
dict2["lista"][1] = 99999
print(dict1)
print(dict2)

""" 
print(len(dict1))
print(list(dict1.keys()))
print(list(dict1.values()))
print(list(dict1.items()))
dict1.setdefault("idade", None)
print(dict1["idade"])

for key in dict1.keys():
    print(key)

for key in dict1.values():
    print(key)

for key, value in dict1.items():
    print(key, value)
 """
