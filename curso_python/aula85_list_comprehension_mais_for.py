l1 = []

for x in range(3):
    for y in range(3):
        l1.append((x, y))
l1 = [(x, y) for x in range(3) for y in range(3)]
print(l1)

l2 = [(x, letra) for letra in "Anderson" for x in range(3)]
print(l2)
