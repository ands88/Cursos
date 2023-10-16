''' 
enumerate - enumra iteráveis (índices)
'''

lista = ['Maria', 'Anderson', 'Neuber']
lista.append ('Aderivaldo')

lista_enumerada = enumerate (lista)

print (lista_enumerada)

#for item in lista_enumerada:
 #   print (item)

#for indice, nome in enumerate(lista):
#    print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print ('FOR da tupla:')
    for indice in tupla_enumerada:
        print (f'\t {indice}')