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

person1 = {
    "nome": "Anderson",
    "sobrenome": "Martins",
}

""" print(person1.get("nome"))
print(person1.get("idade"))
print(person1["nome"]) """

""" nome = person1.pop("nome")
print(nome)
print(person1)

last_key = person1.popitem()
print(last_key)
print(person1) """

""" person1.update(
    {
        "nome": "Neuber",
        "sobrenome": "de Castro",
        "idade": 37,
    }
) """
""" person1.update(nome="Neuber", idade=37) """
list = [["nome", "Neuber"], ["idade", 37]]
person1.update(list)

tuple = (("nome", "Luiz"), ("idade", 69))
person1.update(tuple)
print(person1)
