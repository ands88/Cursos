cpf_inteiro = "36977911840"
digito = cpf_inteiro[len(cpf_inteiro) - 2 :]
cpf = cpf_inteiro[0 : len(cpf_inteiro) - 2]
i = 1
j = 1
numero = ()
total = 0

while j <= 2:
    while i <= len(cpf):
        x = cpf[i * (-1)]
        x = int(x)
        total += x * (i + 1)
        i += 1
    dv = 11 - total % 11
    if dv > 9:
        dv = 0
    dv = str(dv)
    cpf += dv
    if dv == digito[j - 1]:
        print(f"O seu", j, "º dígito é", dv)
    else:
        print("O CPF digitado é inválido.")
    total = 0
    i = 1
    j += 1

print(cpf)
