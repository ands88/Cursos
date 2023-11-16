# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# azul = classe/ verde = função
# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
""" s1 = set()  # vazio

print(s1, type(s1))
print ()

s1 = {"Anderson", 1, 2, 3}  # com dados
print (s1, type(s1))
print()
 """
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
""" l1 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 4, 4, 6, 6]
s1 = set(l1)
l2 = list(s1)

# s1 = {1, 2, 2, 3, 3, 3, 3}

print(s1)
print(l2)
print(6 in s1)
print(2 not in s1) """


# Métodos úteis:
# add, update, clear, discard

""" s1 = set()
s1.add("Anderson")
s1.add(2)
s1.update(("Olá Mundo", 1, 3, 4, 4, 4, 5, 6))
print(s1)
s1.discard("Olá Mundo")
print(s1)
s1.clear()
print(s1) """

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

""" s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s2 - s1
s7 = s1 ^ s2

print(s3)
print(s4)
print(s5)
print(s6)
print(s7) """

# exemplo de uso dos sets
letras = set()

while True:
    letra = input("Digite uma letra:")
    letras.add(letra.lower)

    if "l" in letras:
        print("Parabéns!")
        break

    print(letras)
