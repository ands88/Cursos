nome = 'Anderson Ramos'
altura = 1.82
peso = 110
imc = peso/(altura**2)
... # elipsis, pode ser usado como placeholders

# o uso do 'f' na frente da string é chamado de f-strings, o f vem de formatação

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso:.2f} quilos, e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)