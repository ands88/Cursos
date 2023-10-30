"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma (x, y):
    #definição da função
    print(f'{x=} y={y}', '|', 'x + y = ', x + y)

#print(soma(1, 2)) #essa função está puxando uma função que já tem print nela, 
#por isso não funciona muito bem
soma (1, 2)
soma (2, 4)
soma (y = 3, x = 2)


def soma (x, y, z):
    #definição da função
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y+ z)

soma (1, 2, 3)
soma (2, 4, 6)
soma (z= 4, y = 3, x = 2)