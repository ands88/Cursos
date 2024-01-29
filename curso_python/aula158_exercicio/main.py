"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from classes import Pessoa, Conta, Banco

class Cliente(Pessoa):
    def __init__(self, nome: str, sobrenome: str, idade: int):
        super().__init__(nome, sobrenome, idade)
    
class ContaCorrente(Conta):
    def __init__(self, agencia: int, numero_conta: int, saldo: int | float, cc=True):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self):
        pass

    def depositar(self):
        pass

class ContaPoupanca(Conta):
    def __init__(self, agencia: int, numero_conta: int, saldo: int | float, cp=True):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self):
        pass

    def depositar(self):
        pass

    
cl1 = Cliente ('Anderson', 'Martins', 35)  
conta1 = Conta(23, 12345, 1234.56, cl1.fullname())

print(cl1.fullname())
print(cl1.idade)

print(conta1.informacao_conta())