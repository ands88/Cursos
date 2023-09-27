''' Iterando strings com while'''
#       01234567
nome = 'Anderson' 
tamanho_nome = len(nome)
indice = 0
novo_nome = ''
'''print (nome)
print (nome[5])
print (tamanho_nome)'''

while indice < len(nome):
    letra = nome [indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print (novo_nome)




