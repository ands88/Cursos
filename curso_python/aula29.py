""" Intodução ao tryu/except
try -> tentar executar o código
except -> ocorreu um erro ao tentar executar
"""

# print(1234)
# print(567)
# float("a")

"""numero_str = input("Vou dobrar o número que você digitar: ")
print(numero_str.isdigit())

numero_float = float(numero_str)

print(f"O dobro de {numero_str} é {numero_float * 2}")
"""
"""numero_str = input("Vou dobrar o número que você digitar: ")

if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f"O dobro de {numero_str} é {numero_float * 2}")
else:
    print("Isso não é um número")
"""
numero_str = input("Vou dobrar o número que você digitar: ")
try:
    numero_float = float(numero_str)
    print("FLOAT:", numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2}")
except:
    print("Isso não é um número.")
