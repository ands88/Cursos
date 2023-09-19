# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ') # O input para a execução nele, e só resume quando uma ação é feita
numero_2 = input('Digite outro número: ') 
### esse número pedido no imput vai ser dado como um str 
# nesse caso, as variáveis criadas abaixo servirão para transformar str em int
# Isso vai permitir que o print abaixo entregue a soma, e não a concatenação
###

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')