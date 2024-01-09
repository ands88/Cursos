# method - self, método de instância
# @classmethos - cls, método de classe
# @staticmethod - método estático

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user): #setter
        self.user = user
    
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log (msg):
        print("LOG: ", msg)

c1 = Connection.create_with_auth("Anderson", "1234")
print(c1.user)
print(c1.password)
print(Connection.log('Mensagem'))
""" 
c1 = Connection()
c1.set_user('Anderson')
c1.set_password('123')
print(c1.user)
print(c1.password)"""