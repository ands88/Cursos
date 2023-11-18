# Empacotamento e desempacotamento de dicionários

""" a, b = 1, 2
a, b = b, a

print(a, b)

person = {"nome": "Anderson", "sobrenome": "Martins"}

a, b = person.values()
print(a, b)

(a1, a2), (b1, b2) = person.items()
print(a1, a2)
print(b1, b2)

for key, value in person.items():
    print(key, value)
 """

person = {"nome": "Anderson", "sobrenome": "Martins"}

person_data = {
    "idade": 35,
    "altura": 1.82,
}

complete_data = {**person, "gênero": "masculino", **person_data}

# print(complete_data)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def show_args(*args, **kwargs):
    print("ARGUMENTOS NÃO NOMEADOS:", args)
    for chave, valor in kwargs.items():
        print(chave, valor)


# show_args(76, 2, 3, 4, nome="Anderson", endereço="R. 202")
show_args(**complete_data)
