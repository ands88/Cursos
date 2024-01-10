# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor() - em outras linguagens
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter - getter é um método que chama um atributo, para "proteger" ele dentro da classe
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Pen:
    def __init__(self, color, lid_color):
        self.color = color
        self.lid_color = lid_color

    @property
    def color1(self):
        print("Property")
        return self.color
    
    @property
    def color2 (self):
        print("Color number2")
        return self.lid_color
    
pen = Pen("Blue", "Black")
print(pen.color1,"and", pen.color2)
    