from log import LogPrintMixin

class Eletronico:
    def __init__(self, nome):
        self.nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            print(f'Seu {self.nome}, foi ligado.')
            self._ligado = True

    def desligar(self):
        if self._ligado:
            print(f'Seu {self.nome} foir desligado.')
            self._ligado = False

class Smartphone (Eletronico,  LogPrintMixin):
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self.nome} está ligado.'
            self.log_success(msg)
    
    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self.nome} está desligado.'
            self.log_error(msg)