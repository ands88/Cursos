# decoradores com parâmetros

def decorator_factory (a=None, b=None, c=None):
    def function_factory (func):
        print("decorator 1")

        def nested (*args, **kwargs):
            print('Parâmetro do decorador', a, b, c)
            print('Nested')
            res = func(*args,**kwargs)
            return res
        return nested
    return function_factory

@decorator_factory(1,2,3)
def sum(x, y):
    return x + y

ten_plus_five = sum(10, 5)
print('A soma é:', ten_plus_five)

multiply = decorator_factory()(lambda x, y: x*y)

ten_times_five = multiply(10,5)
print('A multiplicação é:', ten_times_five)
