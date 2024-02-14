# dataclass - O que são dataclasses?
# o módulo dataclass fornece um decorador e funções para criar métodos como __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo usuário.UserWarning
# Em resumo: dataclasses são syntax sugar para criar classes normais,
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass, asdict, astuple, field, fields

@dataclass
class Person:
    nome: str = 'Missing'
    sobrenome: str = 'Not sent'
    idade: int = 0
    enderecos: list[str] = field(default_factory = list)


    # def __post_init__(self):
    #     self.fullname = f'{self.nome} {self.sobrenome}'

    # @property
    # def fullname (self):
    #     return f'{self.nome} {self.sobrenome}'
    
    # @fullname.setter
    # def fullname(self, valor):
    #     nome, sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Person()

    #print(fields(p1))
    print(astuple(p1))
