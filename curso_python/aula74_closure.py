"""
Closure e funções que retornam outras funções
"""


""" def greeting(saudacao, nome):
    return f" {saudacao}, {nome}"


greeting1 = greeting("Boa noite", "Anderson")
greeting2 = greeting("Bom dia", "Neuber")
print(greeting1)
print(greeting2) """


def greeting(
    saudacao,
):
    def greet(nome):
        return f" {saudacao}, {nome}! Tudo bem?"

    return greet


# a função greeting foi criada para criar a função greet que retorna uma saudação e um nome
# o nome foi adiado para a função greet, o que possibilita chamar o nome 'mais tarde'
# chamando o nome mais tarde, podemos colocar uma lista para criar as saudações
# separadamente


greeting_boa_noite = greeting("Boa noite")
greeting_bom_dia = greeting("Bom dia")
greeting_boa_tarde = greeting("Boa tarde")

for name in ["Neuber", "Creusa", "Anderson", "Julia", "Bárbara"]:
    print(greeting_bom_dia(name))
    print(greeting_boa_tarde(name))
    print(greeting_boa_noite(name))
