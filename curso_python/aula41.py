# while/else
string = 'Qualquervalor'
i = 0 #variável representando o índice

while i < len(string):
    letra = string [i]

    if letra == ' ':
        break #o else não é executado quando o comando break for executado
    print (letra)
   # print ('Pula o espaço')
    i += 1
else:
    print ('Espaço não encontrado na string')
print ('Fora do while.')