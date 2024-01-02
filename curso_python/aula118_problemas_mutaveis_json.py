#Problemas dos parâmetros mutáveis em funções no Python
# Sempre que formos criar um parâmatro em python, devemos checar se ele é mutável, se ele for, então não colocamos valor 
# padrão, criamos um None e dentro da função criamos o parâmetro.

def add_clients(name, list = None):
    if list is None:
        list = []
    list.append(name)
    return list


client1 = add_clients("Anderson")
add_clients("Joana", client1)
add_clients("Neuber", client1)
client1.append("Eduardo")
print("Lista 1:", client1)
print()

client2 = add_clients("Joaquim")
add_clients("Maria", client2)
print("Lista 2:", client2)
print()

client3 = add_clients("Mario")
add_clients ("Luiza", client3)
print("Lista 3:", client3)
print()