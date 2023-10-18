''' 
split e join com list e str
split - divide uma string
join - une uma string
strip - corta espaços do começo da frase
'''
'''
frase = 'Olha só que; coisa interessante'
lista_palavras = frase.split('; ')

for i, frase in enumerate(lista_palavras):
    print (lista_palavras[i].strip())
print(lista_palavras)
'''

frase = '    Olha só que     ;     coisa interessante     '
lista_palavras_1 = frase.split('; ')
lista_palavras = []

for i, frase in enumerate(lista_palavras):
   lista_palavras [i] = lista_palavras[i].strip()
print(lista_palavras)