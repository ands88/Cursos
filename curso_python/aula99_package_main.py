#print(__name__)

#from sys import path

#import aula99_package - nesse caso não importa nada, pois está buscando a pasta, e não o módulo em si.

#from aula99_package.modulo import soma_modulo


#print(*path, sep='\n')

#print(soma_modulo(5,8))

#from aula99_package import modulo
#from aula99_package import modulo2

import aula99_package

print(aula99_package.soma_modulo(4,7))