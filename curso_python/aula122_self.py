# Entendendi self em classes Python
# Classe é um "molde" (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe, o self é a própria instância

class Car:
    def __init__(self, name):
        self.name = name
    
    def accelerate (self):
        print(f'{self.name} está acelerando!')

fusca = Car('Fusca')
Car.accelerate(fusca)
#print(fusca.name)
#fusca.accelerate()

celta = Car(name = 'Celta')
Car.accelerate(celta)
#print(celta.name)
#celta.accelerate()