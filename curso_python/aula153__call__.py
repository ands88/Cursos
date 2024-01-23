# método especial __call__, callable é algo que pode ser exxecutado com parênteses
# em classes normais, __call__ faz a instância de uma classe "callable"

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, name):
        print (name, 'is calling', self.phone)

call1 = CallMe ('123456789')
call1('Anderson')