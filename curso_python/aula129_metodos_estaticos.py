# Métodos estáticos (@staticmethod) são métodos que estão dentro da classe,
# mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua classe (São inúteis em Python)

class Class:
    @staticmethod
    def class_function(*args, **kwargs):
        print('Oi', args, kwargs)
    
def func (*args, **kwargs):
    print("oi", args, kwargs)

c1 = Class()
c1.class_function(1, 2, 3)
func(1, 2, 3)
Class.class_function(named=1)
func(named=1)