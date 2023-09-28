''' Calculadora com while'''


'''while True:
    sair = input ('Quer sair? [s]im: ')
    sair = sair.lower()
    sair = sair.startswith ('s')
    print (sair)'''

while True:
    number1 = input ('Digite um número: ')
    number2 = input ('Digite outro número: ')
    operador = input ('Digite um operador (+-/*): ')

    validnumbers = None

    try:
        number1float = float(number1)
        number2float = float (number2)
        validnumbers = True
    except:
        print ('error')
    
    if validnumbers is None:
        print ('Um ou ambos os números são inválidos.')
        continue
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print ('Digite um operador válido')
        continue

    if len (operador) > 1:
        print ('Digite apenas 1 operador.')
        continue
    print ('Calculando...')
    if operador == '+':
        print ('O resultado da sua soma é: ')
        print (f'{number1float} + {number2float} = ', number1float + number2float)
    elif operador == '-':
        print ('O resultado da sua subtração é:') 
        print (f'{number1float} - {number2float} = ',number1float - number2float)
    elif operador == '/':
        print ('O resultado da sua divisão é:') 
        print (f'{number1float} / {number2float} = ',number1float / number2float)
    elif operador == '*':
        print ('O resultado da sua multiplicação é:') 
        print (f'{number1float} * {number2float} = ',number1float * number2float)
    else:
       print ('Algo deu muito errado. Try again!')

    sair = input ('Quer sair? [s]im: ').lower().startswith ('s')

    if sair is True:
        break
