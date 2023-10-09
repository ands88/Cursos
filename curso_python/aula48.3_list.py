"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]

lista.append("Anderson")

print(lista)
print(" ")

del lista[
    -1
]  # deleta algum valor da lista, o -1 vai ser sempre o último valor da lista

print(lista)
print(" ")

lista.insert(
    5, "O Ramos"
)  # o insert recebe dois itens, o primeiro é o índice em que queremos colocar o novo valor, e o segundo é o novo valor

print(lista)
print(" ")
