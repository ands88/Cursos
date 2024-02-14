from abc import ABC, abstractclassmethod, abstractmethod

class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int):
        self._nome = nome
        self._sobrenome = sobrenome
        self.idade = idade
    
    def fullname(self):
        return self._nome + ' ' + self._sobrenome

class Conta(ABC):
    saldo = 0
    def __init__(self, agencia: int, numero_conta: int, cliente, saldo=0):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo
        self._cliente = cliente

    def informacao_conta(self):
        return 'Agência: {}'.format(self._agencia),'Conta: {}'.format(self._numero_conta),'Saldo: {}'.format(self._saldo),'Titular: {}'.format(self._cliente)
    
    @abstractmethod
    def sacar(self):
        raise NotImplementedError ('Implementar sacar!')
    
    def depositar(self, deposito):
       ...

    def mostrar_saldo(self):
        return Conta.saldo



class Banco:
    pass
