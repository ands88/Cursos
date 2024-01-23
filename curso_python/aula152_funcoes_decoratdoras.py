# funcoes decoradoras e decoradores com métodos

def my_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

def add_repr(cls):
    cls.__repr__ = my_repr
    return cls

def my_planet(method):
    def intern (self, *args, **kwargs):
        result = method(self, *args, **kwargs)

        if 'Terra' in result:
            return 'Você está em casa!'

        return result
    return intern


@add_repr
class Planet:
    def __init__(self, name):
        self.name = name

    @my_planet
    def say_name (self):
        return f'The planet is {self.name}'
    


terra = Planet('Terra')
marte = Planet('Marte')

print(terra)
print(terra.say_name())
print()
print(marte)
print(marte.say_name())