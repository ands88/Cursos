
import json
person = {
    "nome": "Anderson R",
    "sobrenome": "Martins",       
    "endereços": [
        {
            "rua": "22", 
            "numero": 53
        }, 
        {
            "rua": "J-1", 
            "numero": 90
        }
    ],
    "altura": 1.82,
    "numeros_preferidos": (3, 8, 9),
    "dev": True,
    "nada": None,     
}

with open('aula117_json.json', 'w') as file:
    json.dump(person, file, ensure_ascii=False, indent=2)

with open('aula117_json.json', 'r') as file:
    person = json.load(file)
    print(person["nome"])
    print(type(person))