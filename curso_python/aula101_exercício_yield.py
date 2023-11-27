# Exercício - Adiando execução de funções
def soma(x, y):
    yield x + y


def multiplica(x, y):
    yield x * y


def criar_funcao(funcao, *args):
    yield funcao(*args)


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

resultado_soma = soma_com_cinco(10)
resultado_multiplica = multiplica_por_dez(4)

print(resultado_soma)
print()
print(resultado_multiplica)

