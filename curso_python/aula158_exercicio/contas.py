from abc import ABC, abstractmethod
    
class Conta(ABC):
    def __init__(self, agencia: str, numero_conta: str, saldo=0):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    def get_agencia(self):
        return self._agencia

    def get_conta(self):
        return self._numero_conta

    def depositar(self, valor: int | float):
        if valor <= 0:
            print('Valor de depósito inválido')
        else:
            self._saldo += valor

    @abstractmethod
    def sacar(self):
        pass



class ContaCorrente(Conta):
    def __init__(self, agencia: str, numero_conta: str, limite=1000, saldo=0):
            super().__init__(agencia, numero_conta, saldo)
            self._limite = limite
            self._agencia = agencia
            self._numero_conta = numero_conta
    
    def depositar(self, valor: int | float):
        super().depositar(valor)
        print(f'Depósito de {valor} realizado na Conta Corrente. Novo saldo da Conta Corrente: {self._saldo}')

    def sacar(self, valor):
        print (f'Seu limite do cheque especial é de R$ {self._limite},00')
        if valor > self._saldo + self._limite or valor <= 0:
            print('Saldo/limite insuficiente ou valor de saque inválido')
        else:
            self._saldo -= valor
            print(f'Saque de {valor} realizado da Conta Corrente. Novo saldo da Conta Corrente: R$ {self._saldo},00')
        


class ContaPoupanca(Conta):
    def __init__(self, agencia: str, numero_conta: str, saldo=0):
        super().__init__(agencia, numero_conta, saldo)
        self._agencia = agencia
        self._numero_conta = numero_conta
    
    def depositar(self, valor: int | float):
        super().depositar(valor)
        print(f'Depósito de {valor} realizado na Conta Poupança. Novo saldo da Conta Poupança: R$ {self._saldo},00')
    
    def sacar(self, valor):
        if valor > self._saldo or valor <= 0:
            print('Saldo insuficiente ou valor de saque inválido')
        else:
            self._saldo -= valor
            print(f'Saque de {valor} realizado da Conta Poupança. Novo saldo da Conta Poupança: R$ {self._saldo},00')
