''' Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal + ou -
Ex.: 0>-100,.1f
conversion flags - !r !s !a
'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{2500.5981546564}')
print(f'{2500.5981546564:,.2f}')
print(f'{2500.5981546564:0>+10.2f}')
print(f'{2500.5981546564:0>+10.2f}')
print(f'{2500.5981546564:0=+10.2f}')
print(f'{variavel!r}')
