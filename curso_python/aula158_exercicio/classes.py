from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int):
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade
    
    def fullname_idade(self):
        return self._nome + ' ' + self._sobrenome + ',' + ' ' + str(self._idade) + ' ' + 'anos'


class Cliente(Pessoa):
    def __init__(self, nome: str, sobrenome: str, idade: int, agencia='', numero_conta_cc='', numero_conta_cp=''):
        super().__init__(nome, sobrenome, idade)
        self.conta_corrente = ContaCorrente(agencia, numero_conta=numero_conta_cc)
        self.conta_poupanca = ContaPoupanca(agencia, numero_conta=numero_conta_cp)


    def fullname_idade(self):
        return super().fullname_idade()
    
    def get_nome(self):
        return self._nome

    def get_cc(self):
        return self.conta_corrente
    
    def get_cp(self):
        return self.conta_poupanca



class Conta(ABC):
    def __init__(self, agencia = '', numero_conta = '', saldo = 0):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self.saldo = saldo
    
    
    def get_agencia(self):
        return self._agencia
    
    def get_conta(self):
        return self._numero_conta

    def depositar(self, valor: int|float):
        if valor <= 0:
            print('Valor de depósito inváido')
        else:
            self.saldo += valor

    def sacar(self):
        raise NotImplementedError ('Implementar sacar!')




class ContaCorrente(Conta):
    def __init__(self, agencia='', numero_conta='', limite = 1000, saldo=0):
        super().__init__(saldo)
        self.limite = limite
        self._agencia = agencia
        self._numero_conta = numero_conta
    
    def depositar(self, valor: int | float):
        super().depositar(valor)
        print(f'Depósito de {valor} realizado na Conta Corrente. Novo saldo da Conta Corrente: {self.saldo}')

    def sacar(self, valor):
        print (f'Seu limite do cheque especial é de R$ {self.limite},00')
        if valor > self.saldo + self.limite or valor <= 0:
            print('Saldo/limite insuficiente ou valor de saque inválido')
        else:
            self.saldo -= valor
            print(f'Saque de {valor} realizado da Conta Corrente. Novo saldo da Conta Corrente: {self.saldo}')
        


class ContaPoupanca(Conta):
    def __init__(self, agencia='', numero_conta='', saldo=0):
        super().__init__(saldo)
        self.agencia = agencia
        self.numero_conta = numero_conta
    
    def depositar(self, valor: int | float):
        super().depositar(valor)
        print(f'Depósito de {valor} realizado na Conta Poupança. Novo saldo da Conta Poupança: {self.saldo}')
    
    def sacar(self, valor):
        if valor > self.saldo or valor <= 0:
            print('Saldo insuficiente ou valor de saque inválido')
        else:
            self.saldo -= valor
            print(f'Saque de {valor} realizado da Conta Poupança. Novo saldo da Conta Poupança: {self.saldo}')

c1 = Cliente('Anderson', 'Ramos', 35, '001', '12345', '54321')

print(c1.fullname_idade())
