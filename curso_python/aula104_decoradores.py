# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (açúcar sintático)

def create_function(func):
    def intern(*args, **kwargs):
        print('Decorando...!')
        for arg in args:
            is_string(arg)

        result = func(*args, **kwargs)
        result += ' Anything'
        print(f'O seu resultado foi {result}.')
        print('Ok. Decorado!')
        return result
    return intern

@create_function
def string_inverted(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param,str):
        raise TypeError('Param deve ser uma string')

invertida = string_inverted('123')
print(invertida)