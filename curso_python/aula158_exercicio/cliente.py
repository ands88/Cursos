
from contas import ContaCorrente, ContaPoupanca

class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int):
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade
    
    def fullname_idade(self):
        return self._nome + ' ' + self._sobrenome + ',' + ' ' + str(self._idade) + ' ' + 'anos'


class Cliente(Pessoa):
    def __init__(self, nome: str, sobrenome: str, idade: int, senha: int, agencia:str, numero_conta_cc:str, numero_conta_cp: str):
        super().__init__(nome, sobrenome, idade)
        # Pass 'agencia' and 'numero_conta_cc' to ContaCorrente constructor
        self._conta_corrente = ContaCorrente(agencia=agencia, numero_conta=numero_conta_cc)
        # Pass 'agencia' and 'numero_conta_cp' to ContaPoupanca constructor
        self._conta_poupanca = ContaPoupanca(agencia=agencia, numero_conta=numero_conta_cp)
        self._senha = senha


    def fullname_idade(self):
        return super().fullname_idade()
    
    def get_nome(self):
        return self._nome

    def get_senha(self):
        return self._senha


    def get_cc(self):
        return self._conta_corrente
    
    def get_cp(self):
        return self._conta_poupanca





