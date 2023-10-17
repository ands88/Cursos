"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os


print("Sua lista de compras!")
lista = []

while True:
    print("Escolha uma opção:")
    opcao = input("1. Adicionar item\n" "2. Retirar item\n" "3. Ver lista\n" "Opção: ")

    if opcao == "1":
        os.system("cls")
        item = input("Digite o item a ser adicionado: ")
        lista.append(item)
        continue

    elif opcao == "2":
        os.system("cls")
        apagar = input("Digite o número do item que quer apagar: \n")

        if apagar.isdigit():
            apagar_int = int(apagar)
            if apagar_int >= 0 and apagar_int < len(lista):
                print(f"{lista[apagar_int]} apagado\n")
                del lista[apagar_int]
            else:
                print("Digite um índice válido.\n")
        else:
            print("Não insira letras!")
            continue

    elif opcao == "3":
        os.system("cls")

        if len(lista) == 0:
            print("Nada para listar")

        for i, valor in enumerate(lista):
            print(i, valor, "\n")

    else:
        print("Escolha uma opção válida.\n")
