# Exercício - sistema de perguntas e respostas

exam = [
    {
        "Pergunta": "Quanto é 2 * 2",
        "Opções": ["a) 6", "b) 8", "c) 2", "d) 4"],
        "Resposta": "d",
    },
    {
        "Pergunta": "Qual o nome do satélite natural da Terra?",
        "Opções": ["a) Europa", "b) Galaxia", "c) Lua", "d) Sol"],
        "Resposta": "c",
    },
    {
        "Pergunta": "Quanto é 1 + 6?",
        "Opções": ["a) 7", "b) 5", "c) 6", "d) 1"],
        "Resposta": "a",
    },
    {
        "Pergunta": "Quanto é 2 * 55?",
        "Opções": ["a) 100", "b) 150", "c) 110", "d) 125"],
        "Resposta": "c",
    },
]

counter_right = 0

for question in exam:
    print(question["Pergunta"])
    for alternatives in question["Opções"]:
        print(alternatives)
    answer_check = input("Digite a alternativa: ")
    # transformar a alternativa em letra minúscula para checagem
    if answer_check.isupper():
        answer_check = answer_check.lower()

    if question["Resposta"] == answer_check and answer_check.isalpha():
        print("Correto!")
        counter_right += 1
    elif question["Resposta"] != answer_check:
        print("Errou!")
    else:
        print("Digite uma alternativa válida")

print(f"Teste finalizado! Você acertou {counter_right} de ", len(exam), "questões.")


""" counter_questions = 0
exam_question = exam[0]["Pergunta"]
exam_alternatives = exam[0]["Opções"]

print(exam_question)

exam_question = exam + [1]["Pergunta"]

print(exam_question) """
""" while counter_questions < len(exam):
    counter_right = 0
    print(f"Questão:", exam_question)

    for alternative in exam_alternatives:
        print(alternative)

    answer_check = input("Digite a alternativa: ")
    # transformar a alternativa em letra minúscula para checagem
    if answer_check.isupper():
        answer_check = answer_check.lower()

    # checar resposta da questão 1 (tester o while, enquanto o counter_right for menor do que o len (exame))
    if exam[0]["Resposta"] == answer_check and answer_check.isalpha():
        print("Correto!")
        counter_right += 1
        counter_questions = +1
    elif exam[0]["Resposta"] != answer_check:
        print("Errou!")
        counter_questions = +1
    else:
        print("Digite uma alternativa válida")
        counter_questions = +1
 """
