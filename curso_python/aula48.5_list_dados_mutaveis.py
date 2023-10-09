"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ["Anderson", "Maria", 1, True, 3.4]
lista_b = lista_a.copy()

lista_a[0] = "Neuber"


print(lista_a)
print(lista_b)
