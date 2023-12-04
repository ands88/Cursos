# decoradores com parâmetros

def decorator (func):
    print("decorator 1")

    def nested (*args, **kwargs):
        print('Nested')
        res = func(*args,**kwargs)
        return res
    return nested

@decorator
def sum(x, y):
    return x + y

ten_plus_five = sum(10, 5)
print(ten_plus_five)

