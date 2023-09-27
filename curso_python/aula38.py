"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
Usando o break, o loop acaba
"""

qdt_linhas = 5
qdt_colunas = 5
linha = 1

while linha <= qdt_linhas:
    coluna = 1
    while coluna <= qdt_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print ('Acabou')