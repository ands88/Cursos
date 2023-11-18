# isinstance = para saber se objeto é de determinado tipo

l1 = ["anderson", 1, 1.1, True, [0, 1, 2], (1, 2), {1, 0}, {"nome": "Anderson"}]

for item in l1:
    if isinstance(item, set):
        item.add(5)
        print("SET", item, isinstance(item, set))

    elif isinstance(item, str):
        item.upper()
        print("STR", item.upper(), isinstance(item, set))

    elif isinstance(item, (int, float)):
        print("NUM", item, item * 2)
    else:
        print("OUTRO", item)
