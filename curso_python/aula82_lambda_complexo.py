def execute(funcao, *args):
    return funcao(*args)


""" def soma(x, y):
    return x + y """


print(execute(lambda x, y: x + y, 3, 4))


""" def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador

    return multiplica """


duplica = execute(lambda m: lambda n: n * m, 2)
print(duplica(3))

print(execute(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
