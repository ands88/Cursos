#frase = 'Estou apredendo a linguagem de programação Python, para que? Deus sabe.'
frase = 'Ooiie'.lower()

#print (frase)
#print (frase.count(' '))

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len (frase):
    letra_atual = frase [i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count (letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    #print (letra_atual, quantas_vezes_a_letra_apareceu)
    i += 1

print (
    'A letra que apareceu mais vezes foi ' 
       f'{letra_apareceu_mais_vezes} que apareceu ' 
       f'{qtd_apareceu_mais_vezes} vezes.'
       )