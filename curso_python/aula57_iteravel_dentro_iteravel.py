""" Lista de listas e seus índices
"""
salas = [
    ["Maria", "Marcos", "Solange"],
    ["Anderson", (0, 10, 20, 30, 40)],
    ["Neuber", "Aderivaldo", "Luiz"],
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(salas[1][1][2])

for sala in salas:
    print(sala)
