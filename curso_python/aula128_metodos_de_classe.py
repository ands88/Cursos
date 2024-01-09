# Métodos de classe + factories (fábricas)
#São métodos onde "self" será "cls", ou seja, ao invés de receber a 
# instância no primeiro parâmetro, recebemos a própria classe

class Person:
    year = 2023 #atributo de classe

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod #decorator
    def class_method (cls):
        print('Hey')
    
    @classmethod
    def create_50 (cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def anonnymous (cls, age):
        return cls("Anônimo", age)

p1 = Person("Anderson", 35)
p2 = Person.create_50("Helen")
p3 = Person.anonnymous(60)

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)

print(Person.year)
Person.class_method()

