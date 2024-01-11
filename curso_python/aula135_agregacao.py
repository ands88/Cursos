# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Cart:
    def __init__(self):
        self._products = []

    def total(self):
        return sum([p.price for p in self._products])

    def add_items(self, *products):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for item in products:
            self._products.append(item)

    def list_products(self):
        print()
        for product in self._products:
            print(product.name, "R$", product.price)
        print()


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


shop_cart = Cart()
p1, p2 = Item('Caneta', 1.20), Item('Camiseta', 20)
shop_cart.add_items(p1, p2)
shop_cart.list_products()
print("R$", shop_cart.total())