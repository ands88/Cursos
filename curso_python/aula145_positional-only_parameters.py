# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

def soma (*args):
    print (sum(args))

soma (1,2,3)
soma (29, 68, 9, 40)

def sum (a, b, /, x, y): # antes da barra, tem que ser posicional, o que vem depois, pode ser nomeado
    print(a+b)
    print(x+y)

sum(1,2, x=5, y=9)

def sum1 (a,b, *args):
    print(args)
    print(a+b)

sum1 (3, 4, "Anderson", "Martins")

def sum2 (a,b, *, c, **kwargs):
    print(kwargs)
    print(a+b+c)

sum2(3,4,c=5, nome="Anderson")