# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions


def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError("Você está tentando dividir por zero")
    return True


def int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f"'{n}' precisa ser um número válido." f"'{tipo_n.__name__}' enviado"
        )
    return True


def divide(n, d):
    int_ou_float(n)
    int_ou_float(d)
    nao_aceito_zero(d)
    return n / d


print(divide("22.5", 2.85))
