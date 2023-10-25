# Desempacotamento em chamadas
# de métodos e funções

string = "ABCD"
lista = ["Anderson", "Neuber", 1, 2, 3, "Luiz"]
tupla = "Python", "é", "legal"
salas = [
    ["Maria", "Marcos", "Solange"],
    ["Anderson", "Creusa", "Barbara"],
    ["Neuber", "Aderivaldo", "Luiz"],
]


# a, b, c, *_, ap, u = lista
# print(a, ap, u)

print(*lista)  # o * funciona como o "desempacotador"
print(*string)
print(*tupla)
print(" ")
print(*salas, sep="\n")
