from cliente import Cliente

clients_data = [
    {'nome': 'João', 'sobrenome': 'Silva', 'idade': 28, 'senha': 1234, 'agencia': '002', 'numero_conta_cc': '67890', 'numero_conta_cp': '98765'},
    {'nome': 'Maria', 'sobrenome': 'Santos', 'idade': 40,  'senha': 0000, 'agencia': '003', 'numero_conta_cc': '11111', 'numero_conta_cp': '22222'},
    {'nome': 'Carlos', 'sobrenome': 'Oliveira', 'idade': 22,  'senha': 1111, 'agencia': '004', 'numero_conta_cc': '33333', 'numero_conta_cp': '44444'},
    {'nome': 'Ana', 'sobrenome': 'Lima', 'idade': 55,  'senha': 2222, 'agencia': '005', 'numero_conta_cc': '55555', 'numero_conta_cp': '66666'},
    {'nome': 'Lucia', 'sobrenome': 'Rodrigues', 'idade': 30,  'senha': 9999, 'agencia': '006', 'numero_conta_cc': '77777', 'numero_conta_cp': '88888'}
]

clients = [Cliente(**data) for data in clients_data]

class Banco:
       
    def __init__(self):
        pass

    def auth (self, senha, conta, agencia):
        for cliente in clients:
          if cliente.get_senha() == senha and (cliente.get_cc().get_conta() == conta or cliente.get_cp().get_conta()) and cliente.get_cc().get_agencia() == agencia:
            return cliente
        print ("Falha na autenticação da Conta Corrente.")
        return None