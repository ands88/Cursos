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
