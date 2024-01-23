# Funções decoradores e decoradores com classes
def add_repr (cls):
    def my_repr(self): #essa função não precisaria estar dentro da add_repr  necesseraiamente
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls


# class MyReprMixin: # classe criada para servir de herança para as outras, para o código não ficar muito grande e repetitivo
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr

@add_repr
class Team:
    def __init__(self, name):
        self.name=name

@add_repr
class Planet:
    def __init__(self, name):
        self.name = name

brasil = Team ('Brasil')
portugal = Team ('Portugal')
terra = Planet('Terra')
marte = Planet('Marte')

print(brasil)

print(marte)