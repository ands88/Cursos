# Precedência dos operadores

# 1. (n + n)  de dentro para fora
# 2. **  potenciação, exponenciação
# 3. * / // % 
# 4. + - 

conta_1 = 1 + 1 ** 5 + 5
conta_2 = (1 + 1) ** (5 + 5)
conta_3 = (1 + int(0.5 + 0.5)) ** (5 + 5) # o int transformou o float para poder realizar a conta

print(conta_1)
print(conta_2)
print(conta_3)
