def find_number(lista):
    ocorrencias = set()

    for numero in lista:
        if numero in ocorrencias:
            return numero
        ocorrencias.add(numero)

    return -1


resultados = []

for lista in lista_de_listas_de_inteiros:
    resultado = find_number(lista)
    resultados.append(resultado)

print(resultados)
