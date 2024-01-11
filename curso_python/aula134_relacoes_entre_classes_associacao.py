# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.

class Writer:
    def __init__(self, name) -> None:
        self.name=name
        self._tool = None

    @property
    def tool(self):
        return self._tool
    
    @tool.setter
    def tool (self, tool):
        self._tool = tool

class Writtingtool:
    def __init__(self,name):
        self.name = name

    def write(self):
        return f'{self.name} is writting'
    
writer = Writer("Anderson")
w_machine = Writtingtool('Writting Machine')
writer.tool = w_machine

print(w_machine.write())
print(writer.tool.write())