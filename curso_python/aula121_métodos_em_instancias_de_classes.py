# Métodos em instâncias de classes Python

class Car:
    def __init__(self, name):
        self.name = name
    
    def accelerate (self):
        print(f'{self.name} está acelerando!')

fusca = Car('Fusca')
print(fusca.name)
fusca.accelerate()

celta = Car(name = 'Celta')
print(celta.name)
celta.accelerate()