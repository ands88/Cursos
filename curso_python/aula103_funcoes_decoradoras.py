# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def create_function(func):
    def intern(*args, **kwargs):
        for arg in args:
            is_string(arg)

        result = func(*args, **kwargs)
        return result
    return intern

def string_inverted(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param,str):
        raise TypeError('Param deve ser uma string')

inverte_string_checando_parametro = create_function(string_inverted)
invertida = inverte_string_checando_parametro('123')
print(invertida)