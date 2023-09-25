''' Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p} [::] início : final : partes - Quando colocando o 
índice do final, colocar 1 a mais do que o queremos pois o Python
para de exibir justamente naquele indice.
Obs.: a função len retorna a qtd de caracteres da str
'''

variavel = 'Olá mundo'
print (variavel[5])
print (variavel [-3])
print (variavel[4:8]) #Quando colocando o índice do final, colocar 1 a mais do que o queremos pois o Python
print (variavel[0:5])
print (variavel[ : 5])

print (len(variavel))

print (variavel[0:len(variavel):2])
print (variavel[ : : -1])