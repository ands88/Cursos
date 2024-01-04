# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

'''string = 'Anderson'  # str
print(string.upper())
print(isinstance(string, str))
'''

class Person:
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname
        ...
p1 = Person('Anderson', 'Martins')
#p1.name = 'Anderson'
#p1.surname = 'Martins'

p2 = Person ('Neuber', 'Castro')

print (p1.name)
print (p1.surname)
print (p2.name)
print (p2.surname)
