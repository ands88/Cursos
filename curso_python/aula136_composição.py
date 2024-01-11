# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Client:
    def __init__(self, name):
        self.name = name
        self.address = []

    def insert_address(self, street, number):
        self.address.append(Address(street, number))
    
    def list_address(self):
       for address in self.address:
           print(address.street, address.number)
    
class Address:
    def __init__ (self, street, number):
        self.street = street
        self.number = number

    def __del__(self):
        print("Apagando", self.street, self.number)

client1 = Client ("Anderson")
client1.insert_address("Av. 1", 60)
client1.insert_address("Rua 33", 521)
client1.list_address()

print("FIM DO CÓDIGO")