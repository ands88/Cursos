""" 
Operação ternária (conficional de um linha)
<valor> if <condição> else <outro valor>
"""
condicao = 10 == 11
variavel = "Valor" if condicao else "Outro valor"
print(variavel)
print(" ")

digito = 9
novo_digito = digito if digito <= 0 else 0

print(novo_digito)
