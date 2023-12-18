import random

# Lista de palavras secretas
palavras_secretas = ["python", "programacao", "computador", "openai", "inteligencia"]

# Escolhe uma palavra secreta aleatória
palavra_secreta = random.choice(palavras_secretas)

# Inicializa uma lista para armazenar as letras adivinhadas corretamente
letras_corretas = []

print("Bem-vindo ao jogo de adivinhação de palavras!")
print("Adivinhe a palavra secreta. Ela tem", len(palavra_secreta), "letras.")

tentativas = 0

while True:
    letra = input("Digite uma letra: ").lower()  # Converte a letra para minúscula
    
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite uma única letra válida.")
        continue

    if letra in letras_corretas:
        print("Você já tentou essa letra.")
        continue
    
    if letra in palavra_secreta:
        letras_corretas.append(letra)
        print("Letra correta!")
    else:
        print("Letra incorreta.")

    tentativas += 1  # Incrementa o contador de tentativas

    palavra_atual = ""
    for letra_palavra in palavra_secreta:
        if letra_palavra in letras_corretas:
            palavra_atual += letra_palavra
        else:
            palavra_atual += "*"
    
    print("Palavra atual: " + palavra_atual)
    print("Tentativas até agora:", tentativas)

    if set(letras_corretas) == set(palavra_secreta):
        print("Parabéns! Você adivinhou a palavra secreta:", palavra_secreta)
        break

    #continuar = input("Deseja continuar tentando? (S/N): ").lower()
    #if continuar != "s":
     #   print("Você desistiu. A palavra secreta era:", palavra_secreta)
      #  break
