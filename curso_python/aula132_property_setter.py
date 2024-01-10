# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Pen:
    def __init__(self, color):
        self._cor = color #atributos com _ - não é para ser utilizado
        self._lid_color = None

    @property
    def color (self):
        print ("Property")
        return self._cor
    
    @color.setter
    def color (self, value):
        print("Dentro do Setter.", "A cor é", value)
        self._cor = value
    
    @property
    def lid_color(self):
        self._lid_color
    
    @lid_color.setter
    def lid_color(self, value):
        self._lid_color = value



""" def show (pen):
    return pen.color """

pen = Pen("Azul")
pen.color = "Rosa"
pen.lid_color = "Azul"

#getter -> obter valor

print(pen.color)
print(pen.lid_color)


