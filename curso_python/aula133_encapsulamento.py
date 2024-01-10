# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Foo:
    def __init__(self):
        self.public= "Isso é público!"
        self._protected = "Isso é protegido"
        self.__private = "Isso é privado"

    def public_method(self):
        #self.protected_method()
        #print(self._protected)
        print(self.__private)
        return "Método Público"

    def _protected_method(self):
        return "Método Protegido"

    def __private_method(self):
        return "Método privado"


f=Foo()

#print(f._protected)
#print(f._protected_method())
#print(f.public)
print(f.public_method())
# print(f.__private_method()) -- AttributeError: 'Foo' object has no attribute '__private_method'. Did you mean: '_Foo__private_method'?
print(f._Foo__private_method())