"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_digitado = input("Digite um número: ")
# criei uma variável com o input de um número qualquer
if numero_digitado.isdigit():
    numero_digitado_int = int(numero_digitado)
    modulo = numero_digitado_int % 2
    if modulo == 0:
        # criei uma condição, caso o resto do móduilo fosse 0, o número seria divisivel por 2, ou seja, par.
        print("Seu número é par.")  # imprimindo essa mensagem caso fosse par
    else:  # caso o módulo retornasse algum valor que não fosse 0, o número é impar
        print("Seu número é impar.")
    # criei uma variável transformando o número criado (str) em int
    # print(type(numero_digitado_int)) # checagem para ver se o número estava sendo de fato transformado em int

    # criei uma variável para checagem se o número é divisivel por 2 (não existe resto na divisão por 2)\
# sendo assim, par
else:
    print("Você não digitou um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print(" ")

hora_digitada = input("Digite somente a hora: ")  # criei uma variável para a hora str

# variável para tranformar a str da hora digitada em int
if hora_digitada.isdigit():
    hora_digitada_int = int(hora_digitada)
    if hora_digitada_int >= 0 and hora_digitada_int <= 11:
        print("Bom dia!")
    elif hora_digitada_int >= 12 and hora_digitada_int <= 17:
        print("Boa tarde!")
    elif hora_digitada_int >= 18 and hora_digitada_int <= 23:
        print("Boa noite!")
else:
    print("Você não digitou um horário válido!")
    # condições para fazer a checagem da hora digitada e, caso
    # a hora digitada não esteja entre os valores aceitos, uma mensagem de erro é exibida


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
print(" ")

nome_digitado = input("Digite seu primeiro nome: ")  # variável para pegar um nome
tamanho_do_nome = len(nome_digitado)
# variável para analisar a quantidade de caracteres o nome da variável
# anterior tem

if tamanho_do_nome >= 1 and tamanho_do_nome <= 4:
    print("Seu nome é curto.")
elif tamanho_do_nome == 5 and tamanho_do_nome == 6:
    print("Seu nome tem um tamanho normal.")
else:
    print("Seu nome é grande.")
    # condições para checagem da quantidade de caracteres e mensagem
    # dependendo da quantidade no nome digitado
