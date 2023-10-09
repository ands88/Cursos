"""
Exercício
Exiba os índices da lista
"""


lista = ["Anderson", "Creusa", "Barbara", "Julia"]
lista.append(input("Digite um nome aqui: "))

index = range(
    len(lista)
)  # toda modificação na lista deve ser feita antes dessa variável

for indice in index:
    print(indice, lista[indice], type(lista[indice]))
