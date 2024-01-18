# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
with open('aula149_context_manager.txt', 'w') as arquivo:
    ...

class MyOpen:
    def __init__(self, file_path, mode) -> None:
        self.file_path = file_path
        self.mode = mode
        self._file = None
        print('Init')

    def __enter__(self):
        print('Enter, abrindo o arquivo')
        self._file = open(self.file_path, self.mode, encoding="utf8")
        return self._file

    def __exit__(self, class_exception, exception_, traceback_):
        print('Exit, fechando arquivo')
        self._file.close()
    

with MyOpen('aula149_context_manager.txt', 'w') as file:
    file.write('Cool beans')
    print('With', file)
    