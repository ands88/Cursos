# Exercício - sistema de perguntas e respostas

questions = [
    {
        "Pergunta": "Qual a akuma no mi do Monkey D. Luffy?",
        "Opções": [
            "Bara Bara no mi",
            "Gomu Gomu no mi",
            "Pika Pika no mi",
            "Doa Doa no mi",
        ],
        "Resposta": "Gomu Gomu no mi",
    },
    {
        "Pergunta": "Quantas esferas do dragão existem na Terra?",
        "Opções": ["7", "14", "8", "10"],
        "Resposta": "7",
    },
    {
        "Pergunta": "Qual o nome da zanpakutou de Ichigo?",
        "Opções": ["Shiranui", "Tobimaru", "Zamasu", "Zangetsu"],
        "Resposta": "Zangetsu",
    },
    {
        "Pergunta": "Quanto é 2 * 55?",
        "Opções": ["100", "150", "110", "125"],
        "Resposta": "110",
    },
]


def fazer_pergunta(pergunta, opcoes, resposta_correta):
    print(pergunta)
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")

    resposta_usuario = input("Escolha a opção correta (1-4): ")
    try:
        resposta_usuario = int(resposta_usuario)
        if 1 <= resposta_usuario <= 4:
            if opcoes[resposta_usuario - 1] == resposta_correta:
                print("Resposta correta!\n")
                return True
            else:
                print("Resposta incorreta!\n")
                return False
        else:
            print("Opção inválida. Tente novamente.\n")
            return fazer_pergunta(pergunta, opcoes, resposta_correta)
    except ValueError:
        print("Entrada inválida. Tente novamente.\n")
        return fazer_pergunta(pergunta, opcoes, resposta_correta)


pontuacao = 0

for pergunta in questions:
    if fazer_pergunta(pergunta["Pergunta"], pergunta["Opções"], pergunta["Resposta"]):
        pontuacao += 1

print(f"Você acertou {pontuacao} de {len(questions)} perguntas.")
