""" Exemplo

Este módulo contém funções e exemplos de documentação de funções.
A função soma já é bem conhecida."""

var1 = 1

def soma (x: int| float, y: int|float) -> int|float:
    """ soma x e y
    
    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float

    :return: A soma entre x e y
    :rtype: int or float
    """
    return x + y

def multiplicacao(x: int| float,
                  y: int | float,
                  z: int | float | None = None
                  ) -> int | float:
    """ Multiplica x, y e/ou z
    
    Multiplica x e y. Se z for enviado, mutiplica x, y e z
    """
    if z is None:
        return x * y
    return x * y * z

var2 = 2
var3 = 3
var4 = 4