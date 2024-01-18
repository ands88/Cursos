# __new__ e __init__ em classes Python
# __new é responsável por criar e retornar o novo objeto. Por isso, recebe cls
# __new__ deve retornar o novo código
# __init__ é reponsável por inicializar a instância. Por isso init recebe self
# __init__ Náo deve retornar nada (None)
# objetct é a super classe de uma classe

class A:

    def __new__(cls):
        print('Antes de criar a instância')
        instancia = super().__new__(cls)
        print('Depois de criar a instância')
        return instancia
        
    def __init__(self) -> None:
        print('Dentro do init')

    def __repr__(self):
        return "A()"
    
# a = object.__new__(A)
# a.__init__()

# tudo isso é igual a:

a = A()
print(a)