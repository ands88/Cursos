# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Coordinate:
    def __init__(self, x, y, z = 'String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'{self.x}, {self.y}'
        
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}(x = {self.x!r}, y={self.y!r}, z={self.z!r})'

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Coordinate(new_x, new_y)
    
    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y
        return result_self > result_other

p1 = Coordinate(1, 2)
p2 = Coordinate (876, 345)
p3 = p1 + p2

print(p1)
print(repr(p2))
print(f'{p1!r}')
print(p3)
print ('P1 é maior que P2', p1 > p2)
print('P2 é maior que P1', p2 > p1)