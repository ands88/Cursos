import json
from aula127_a_exercício_salvando_class_em_JSON import FILE_PATH, Person

with open(FILE_PATH, "r") as file:
    data = json.load(file)

    for person in data:
        print(person)