"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

"""cpf = "006968261"
digito = "51"
i = 1
numero = ()
total = 0

while i <= len(cpf):
    x = cpf[i * (-1)]
    x = int(x)
    total += x * (i + 1)
    i += 1
    print(total)

dv = (10 * total) % 11
if dv > 9:
    dv = 0

print(dv)
dv = str(dv)
if dv == digito[0]:
    print("Primeiro dígito está válido!")
"""

cpf_inteiro = "00696826151"
digito = cpf_inteiro[len(cpf_inteiro) - 2 :]
cpf = cpf_inteiro[0 : len(cpf_inteiro) - 2]
i = 1
numero = ()
total = 0
print(cpf_inteiro)

while i <= len(cpf):
    x = cpf[i * (-1)]
    x = int(x)
    total += x * (i + 1)
    i += 1

dv = 11 - total % 11
if dv > 9:
    dv = 0


dv = str(dv)
if dv == digito[0]:
    print(f"O seu primeiro dígito é", dv)
    print("Primeiro dígito está válido!")
else:
    print("O CPF digitado é inválido.")
