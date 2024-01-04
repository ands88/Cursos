# Escopo da classe e de métodos

class  Animal:
    #nome = "Leão"
    def __init__(self, name):
        self.nome = name
        variable = "valor" # essa varável é do escopo do método init, não pode ser usada em outros métodos dessa classe
        print(variable)
    
    def eating (self, food):
        return f'{self.nome} está comendo {food}'
    
    def execute (self, *args, **kwargs):
        return self.eating(*args, **kwargs)
    
leao = Animal(name="Leão")
print (leao.nome)
print(leao.execute('maçã'))