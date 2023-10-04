"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar 
apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra 
secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

import random 

secret_words = ['dungeon', 'learning', 'programmimg', 'smart', 'cool'] # criada uma variável
#para definir uma lista de palavras, por isso é usado os colchetes, para criar lista
secret_word = random.choice(secret_words) # variável criada para selecionar uma palavra
#aleatória da lista de palavras
right_letters = [] # inicializa uma lista para armazenagem das tentativas
times_tried = 0 # número atual de tentativas

print ('Quero jogar um jogo com você...')
print ('Adivinhe a palavra secreta! Ela tem', len (secret_word), 'letras.')

while True:
    letter = input ('Digite uma letra: ')
    if len (letter) != 1 or not letter.isalpha():
        print ('Digite uma letra válida aí, parceire.')
        continue
    if letter in right_letters:
        print('Você já digitou essa letra, tente novamente')
        continue
    if letter in secret_word:
        right_letters.append(letter)
        print('Acertou uma letra.')
    else:
        print('Letra errada, tente uma diferente')

    times_tried += 1
