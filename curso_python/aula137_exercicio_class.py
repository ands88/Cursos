# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante
        self.fabricante.carros_fabricados(self)
    
    def exibir_carro (self):
        print (f'Nome do carro: {self.nome}')
        print(f"Tipo do Motor: {self.motor.nome}")
        print(f"Fabricante: {self.fabricante.nome}")

class Motor:
    def __init__ (self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self,nome):
        self.nome = nome
        self.carros = []
    
    def carros_fabricados (self, carro):
        self.carros.append(carro)


motor1 = Motor('Tipo X')
motor2 = Motor ('Tipo Y')
fabricante1 = Fabricante('Fabricante A')
carro1 = Carro('Carro 1', motor1, fabricante1)
carro2 = Carro('Carro 2', motor2, fabricante1)

carro1.exibir_carro()
print("------------------")
carro2.exibir_carro()