import os

exam = [
    {
        "Pergunta": "Quanto é 2 * 2?",
        "Opções": ["6", "8", "2", "4"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Qual o nome do satélite natural da Terra?",
        "Opções": ["Europa", "Galaxia", "Lua", "Sol"],
        "Resposta": "Lua",
    },
    {
        "Pergunta": "Quanto é 1 + 6?",
        "Opções": ["7", "5", "6", "1"],
        "Resposta": "7",
    },
    {
        "Pergunta": "Quanto é 2 * 55?",
        "Opções": ["100", "150", "110", "125"],
        "Resposta": "110",
    },
]

alternativas = ["a", "b", "c", "d"]

counter_right = 0
pergunta_i = 1


def q():
    print(" ")


for question in exam:
    os.system("cls")
    print(f"Acertos: {counter_right} de {len(exam)}")
    print(f"Questão: {pergunta_i} de {len(exam)}")

    q()
    pergunta_i += 1
    print(question["Pergunta"])
    letra = "a"

    q()
    for alternatives in question["Opções"]:
        print(letra + ") " + alternatives)
        letra = chr((ord(letra) + 1))

    q()
    answer_check = input("Digite a alternativa: ")
    # transformar a alternativa em letra minúscula para checagem
    while not answer_check.lower() in alternativas:
        answer_check = input("Digite a alternativa válida: ")

    if (
        question["Opções"][ord(answer_check.lower()) - 97] == question["Resposta"]
        and answer_check.isalpha()
    ):
        counter_right += 1


os.system("cls")
q()
q()
q()
q()
print(
    f"      Teste finalizado! Você acertou {counter_right} de {len(exam)} questões!!!     "
)
q()
q()
q()
q()
