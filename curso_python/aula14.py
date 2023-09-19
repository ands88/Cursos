a= 'AAAAA'
b= 'BBBBB'
c= 1.1
string = 'a={nome1} a={nome1} b={nome2} b={nome2} c={nome3:.4f} c={nome3:.4f}'
formato = string.format(
    #ao nomear o argumento, ele é considerado um parâmetro
    nome1=a, 
    nome2=b, 
    nome3=c
    )

print(formato)