# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations

pessoas = ['Anderson', 'Neuber', 'João', 'Carlos']
camisetas = ['preta', 'branca']

print(*list(combinations(pessoas,2)), sep='\n')
