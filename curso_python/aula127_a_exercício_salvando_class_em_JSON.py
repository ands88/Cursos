# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias da classe com os dadoos salvos
# Faça em arquivos separados
import json

FILE_PATH = 'aula127_Json_person.json'

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Anderson", 35)
p2 = Person("Neuber", 37)
p3 = Person("José", 40)
db = [vars(p1), vars(p2), vars(p3)]


with open("aula127_Json_person.json", "w") as file:
    json.dump(db, file, ensure_ascii=False, indent=2)
   
