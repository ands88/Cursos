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
        "Opções": ['a) 7', 'b) 5', 'c) 6', 'd) 1'],
        "Resposta": "a",
    },
    {
        "Pergunta": "Quanto é 2 * 55?",
        "Opções": ["a) 100", "b) 150", "c) 110", "d) 125"],
        "Resposta": "c",
    },
]


counter_right = 0


print(f'Questão:', exam[0]['Pergunta'])

for alternative in exam[0]['Opções']:
    print (alternative)

answer_check = input ('Digite a alternativa: ')
#transformar a alternativa em letra minúscula para checagem
if answer_check.isupper():
    answer_check = answer_check.lower()

#checar resposta da questão 1 (tester o while, enquanto o counter_right for menor do que o len (exame))
if exam[0]['Resposta'] == answer_check and answer_check.isalpha():
    print('Correto!')
    counter_right += 1
elif exam[0]['Resposta'] != answer_check:
    print ('Errou!')
else:
    print('Digite uma alternativa válida')


    
# função para fazer pergunta
def asking():
    ...
