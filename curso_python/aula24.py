# Operadores in e not in
# Strings são iteráveis (pode navegar item por item)
#  0 1 2 3 4 5 6 7
#  A n d e r s o n
# -8-7-6-5-4-3-2-1

nome = input ('Digite seu nome: ')
encontrar = input (f'O que deseja saber sobre o nome {nome}? ')

"""print (nome[5])
print (nome [-2])
print (10 * '--')
print ('r' in nome)
print ('l' in nome)
print (10 * '--')
print ('ders' not in nome)
print ('man' not in nome)"""

if encontrar in nome:
    print (f'{encontrar} está no nome {nome}.')
else:
    print (f'{encontrar} não está no nome {nome}.')
