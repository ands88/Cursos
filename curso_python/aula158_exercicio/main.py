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
from classes import Cliente, ContaCorrente, ContaPoupanca

clients_data = [
    {'nome': 'João', 'sobrenome': 'Silva', 'idade': 28, 'agencia': '002', 'numero_conta_cc': '67890', 'numero_conta_cp': '98765'},
    {'nome': 'Maria', 'sobrenome': 'Santos', 'idade': 40, 'agencia': '003', 'numero_conta_cc': '11111', 'numero_conta_cp': '22222'},
    {'nome': 'Carlos', 'sobrenome': 'Oliveira', 'idade': 22, 'agencia': '004', 'numero_conta_cc': '33333', 'numero_conta_cp': '44444'},
    {'nome': 'Ana', 'sobrenome': 'Lima', 'idade': 55, 'agencia': '005', 'numero_conta_cc': '55555', 'numero_conta_cp': '66666'},
    {'nome': 'Lucia', 'sobrenome': 'Rodrigues', 'idade': 30, 'agencia': '006', 'numero_conta_cc': '77777', 'numero_conta_cp': '88888'}
]

clients = [Cliente(**data) for data in clients_data]


# class Banco:
       
#     def __init__(self):
#         pass

#     def auth_cc (self, cliente, conta_c, agencia):
#        if cliente in self.lista_clientes and conta_c in self.lista_cc and agencia in self.lista_agencias:
#            print ("Conta Corrente autenticada!")
#            return True
#        else:
#            print ("Falha na autenticação da Conta Corrente.")
#            return False

#     def auth_cp (self, cliente, conta_p, agencia):
#        if cliente in self.lista_clientes and conta_p in self.lista_cp and agencia in self.lista_agencias:
#            print ("Conta Poupança autenticada!")
#            return True
#        else:
#            print ("Falha na autenticação da Conta Poupança.")
#            return False

print(clients[1].get_cp().get_agencia())