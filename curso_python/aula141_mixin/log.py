# abstração: classe Log para logar algo no programa
# herança - é um (LogFileMixin é Log)
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método _log')
    
    def log_error(self, msg):
        self._log(f'Error: {msg}')
        
    def log_success (self, msg):
        self._log(f'Success: {msg}')

class LogFileMixin(Log): # a utilização do "Mixin", quer dizer que essa classe servirá para adicionar coisas em outras classes que podem não der da família
    def _log(self, msg):
        msg_format = f'{msg} Dentro da classe {self.__class__.__name__}'
        print("Salvando no log", msg_format)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_format)
            arquivo.write('\n')
        

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} Dentro da classe {self.__class__.__name__}')

if __name__ == '__main__': # se o nome for igual ao nome do módulo, segue com o teste.
    lf = LogFileMixin()
    lf.log_error('Something')
    lf.log_success('Que legal')

    lp = LogPrintMixin()
    lp.log_error('Something')
    lp.log_success('Que legal')

