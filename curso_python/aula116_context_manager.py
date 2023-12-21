import os
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

file_path = '/Users/andersonrmartins/Documents/GitHub/Cursos/curso_python/'
file_path += 'arquivo116.txt'

#arquivo = open(file_path, 'w')

#arquivo.close()

# with open(file_path, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('Lendo....')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='') #utilizado para remover a quebra de linha no final 
#     print(arquivo.readline().strip()) #utilizado para remover a quebra de linha no final 
#     print(arquivo.readline().strip())
#     print("READLINES")
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())


# print('#' * 20)

# with open(file_path, 'r') as arquivo:
#     print(arquivo.read())

with open(file_path, 'w') as arquivo: #usando o "w", quando é executado, o arquivo é totalmente apagado e escrito novamente
    arquivo.write('Atenção\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

#no windows, o encoder tem que ser "chamado" no código para não dar erro.
# with open(file_path, 'w', encoder='utf-8') as arquivo:
    
# os.unlink(file_path) #Apaga o arquivo 
# os.rename(file_path, 'aula116-2.txt') #renomeia o arquivo
