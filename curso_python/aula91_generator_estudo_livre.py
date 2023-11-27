def topten():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n +=1
    

values = topten()


for i in values:
    print (i)


#gerar letras minúsculas

'''import string

def letters ():
    for letter in string.ascii_lowercase:
        print (letter)

for letter_lower in letters():
    print(letter_lower)'''


#checar números primos

import itertools

def prime_numbers():
    yield 2 #primeiro número primo
    prime_cache = [2] #cache dos números primos

# Loop para os n[umeros primos positivos

    for n in itertools.count(3, 2):
        is_prime = True

        #checagem para a divisão do número primo
        for p in prime_cache:
            if n % p == 0:
                is_prime = False
                break
            #checagem se o número é primo
        if is_prime:
            prime_cache.append(n)
            yield n

for p in prime_numbers():
    print(p)
    if p>200:
        break


squares = (x**2 for x in itertools.count(1))

for n in squares:
    print(n)
    if n > 500:
        break