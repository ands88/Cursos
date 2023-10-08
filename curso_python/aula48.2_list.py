"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40, 50, 60]

print(lista)

lista[2] = 300  # modifica o item da lista


del lista[1]  # deleta aquele item alocado no índice indicado

print(lista)
print(lista[2])  # imprime aquele índice


lista.append(70)  # adiciona um item ao final da lista

print(lista)

lista.append(80)
print(lista)
lista.pop()  # remove o último item da lista
lista.append(999)

print(lista)

ultimo_valor = lista.pop()
print(lista, "Removido", ultimo_valor)
