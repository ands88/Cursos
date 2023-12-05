#ordem dos decoradores

def decorator_parameters (nome):
    def decorator (func):
        print("Decorator:", nome)

        def new_function (*args, **kwargs):
            res = func(*args,**kwargs)
            final = f'{res}{nome}'
            return final
        return new_function
    return decorator

@decorator_parameters(nome=' Quarto')
@decorator_parameters(nome=' Terceiro')
@decorator_parameters(nome=' Segundo')
@decorator_parameters(nome=' Primeiro')
def sum(x, y):
    return x + y

ten_plus_five = sum(10, 5)
print('A soma é:', ten_plus_five )
