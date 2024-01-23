# super () é a super classe na suyb classe
# Classe principal (Pessoa)
# -> super class, base class, parent class
# Classes filhas (Cliente)
# -> sub class, child class, derived class
'''class MyStr(str):
    def upper(self):
        print("Chamou o método UPPER criado")
        retorno =  super().upper()
        print("Depois do retorno à função upper")
        return retorno

string = MyStr("anderson - usando o upper")
print(string.upper())
'''

class A:
    atributo_a = "Valor A"
    def metodo(self):
        print ("A")

class B(A):
    atributo_b = "Valor B"
    def metodo (self):
        print("B")

class C(B):
    atributo_c = "Valor C"
    def metodo (self):
        super(B, self).metodo() # chama a classe acima do B, ou seja, o mátodo da classe A
        super().metodo() # chama a classe acima da classe atual, a C, ou seja, chama oo método da classe B
        print ("C")

c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()

