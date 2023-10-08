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

secret_words = [
    "dungeon",
    "learning",
    "programmimg",
    "smart",
    "cool",
]  # criada uma variável
# para definir uma lista de palavras, por isso é usado os colchetes, para criar lista
secret_word = random.choice(secret_words)  # variável criada para selecionar uma palavra
# aleatória da lista de palavras
right_letters = []  # inicializa uma lista para armazenagem das tentativas certas
times_tried = 0  # número atual de tentativas
i = 0


print("Quero jogar um jogo com você...")
print("Adivinhe a palavra secreta! Ela tem", len(secret_word), "letras.")

# while i < len(secret_word):
#   str(right_letters.append("*"))
#   i += 1


while True:
    #  print(secret_word, right_letters, 'Tentativas: ', times_tried)
    print("Tentativas: ", times_tried)
    letter = input("Digite uma letra: ").lower()
    print(" ")
    word = ""

    if len(letter) != 1 or not letter.isalpha():
        print("Digite uma letra válida aí, parceire.")
        print(" ")

        times_tried += 1
        continue

    if letter in right_letters:
        print("Você já digitou essa letra, tente novamente")
        print(" ")

        times_tried += 1
        continue

    if letter in secret_word:
        right_letters.append(letter)
        print("Acertou uma letra.")
        print(" ")

    for letter_word in secret_word:
        if letter_word in right_letters:
            word += letter_word
        else:
            word += "*"

    else:
        print("Letra errada, tente uma diferente")
        print(" ")

    print("Palavra atual: " + word)
    print(" ")
    # for i in len(secret_word):
    #      if secret_word[i] == letter:
    #          right_letters[i] == letter

    if set(right_letters) == set(secret_word):
        print(
            "Você acertou a palavra: ",
            secret_word,
            " com ",
            times_tried,
            " tentativas!",
        )
        break

    times_tried += 1
