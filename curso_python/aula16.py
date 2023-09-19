# if / elif      / else
# se / se não se / se não

entrada = input ('Você quer ir para a "direita" ou "esquerda"? ')

if entrada == 'direita':
    print ('Você chegou a uma sala escura')
# elif depende do "if"
elif entrada == 'esquerda':
    print ('Você chegou a um beco sem saída') 
elif entrada == 'cima':
    print ('Você encontrou um alçapão no teto')
    input ('Deseja subir? ')
 #   if cima == 'sim': # Esse código está dando problemas ainda. 
 #       print('Você encontrou uma saída') # Preciso aprender a resolver
# else é sempre a última opção, depende do if também
else:
    print ('Você decidiu não ir a lugar algum.')

print ('Sua aventura acabou.')