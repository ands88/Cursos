# __dict__ e vars para atributos de instância

class Person:
    current_year = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_birth_year(self):
        return Person.current_year - self.age
    

data = {'name': 'Anderson', 'age': 35}
p1 = Person (**data)

p1.__dict__['outra'] = 'coisa'

print(p1.__dict__)
print(vars(p1))
print(p1.outra)