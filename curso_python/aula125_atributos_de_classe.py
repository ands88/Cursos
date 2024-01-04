# Atributos de classe

class Person:
    current_year = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_birth_year(self):
        return Person.current_year - self.age
    
p1 = Person('Anderson', 35)
p2 = Person('Helena', 12)


print(p1.get_birth_year())
print(p2.get_birth_year())