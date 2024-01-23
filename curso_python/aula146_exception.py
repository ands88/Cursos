# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    ...

class AnotherError(Exception):
    ...

def raise_exception():
    exception_= MyError('a', 'b', 'c')
    exception_.add_note('Olha a anotação 1 - Você errou isso aqui')
    raise exception_

try:
    raise_exception()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = AnotherError('Lançando outro erro')
    exception_.add_note ('Uma nova anotação')
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error