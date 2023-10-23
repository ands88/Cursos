""" 
split e join com list e str
split - divide uma string
join - une uma string
strip - corta espaços do começo da frase
"""
"""
frase = 'Olha só que; coisa interessante'
lista_palavras = frase.split('; ')

for i, frase in enumerate(lista_palavras):
    print (lista_palavras[i].strip())
print(lista_palavras)
"""

frase = "    Olha só que     ;     coisa interessante     "
lista_palavras_1 = frase.split("; ")
lista_palavras = []

for i, frase in enumerate(lista_palavras_1):
    lista_palavras.append(lista_palavras_1[i].strip())

# print(lista_palavras_1)
# print(lista_palavras)

frase_unida = " ".join(lista_palavras)
print(frase_unida)
