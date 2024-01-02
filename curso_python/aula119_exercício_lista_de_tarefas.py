# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

task_list = []
deleted = []

print('SUA LISTA DE TAREFAS!')
while True:
    print(
          "1. Adicionar \n"
          "2. Listar \n"
          "3. Remover \n"
          "4. Desfazer \n"
          )
    choices = input("Escolha o número da ação: ")

    if choices == '1' or choices == 'adicionar':
        task_list.append(input('Adicione uma tarefa: '))
    
    elif choices == '2' or choices == 'listar':
        print('SUA LISTA DE TAREFAS: \n')
        if len(task_list) == 0:
            print('Sua lista de tarefas está vazia. \n')
        else: 
            for task in task_list:
                print(task)
                print()
    
    elif choices == '3' or choices == 'remover':
        try:
            deleted.append(task_list.pop())
            print(deleted)
        except IndexError:
            print('Sem tarefas para remover! \n')
    
    elif choices == '4' or choices == 'desfazer':
        try:
            task_list.append(deleted[-1])
            deleted.pop()
        except IndexError:
            print('Sem ações para desfazer! \n')
    
    elif choices == 'limpar':
        task_list.clear()
        deleted.clear()
        print('Sua lista de tarefas foi excluída! \n')
    
    elif choices != '1'and choices != '2'and choices != '3'and choices != '4'and choices != 'limpar': 
        print('Escolha uma opção válida, utilize apenas as opções fornecidas. \n')