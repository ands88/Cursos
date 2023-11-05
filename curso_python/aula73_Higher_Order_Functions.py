"""
Higher Irder Functions
Funções de primera classe
"""


def greeting(msg, nome):
    return f"{msg}, {nome}!"


def execute(function, *args):
    return function(*args)


print(execute(greeting, "Boa Noite", "Anderson"))
print(execute(greeting, "Boa Noite", "Neuber"))
