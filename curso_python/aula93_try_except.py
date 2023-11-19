# Try, except, else e finally


try:
    a = 18
    b = 0
    print("Linha 1")
    c = a / b
    print("Linha 2")  # essa linha não é executada pois é lido só até o erro
except ZeroDivisionError:
    print("Dividiu por zero")
except NameError:
    print("Nome b não está definido")
except (TypeError, IndexError) as error:
    print("TypeError + IndexError")
    print("ERRO: ", error)
    print("Nome:", error.__class__.__name___)
except Exception:  # o exception é a 'maior' exceção
    print("ERRO DESCONHECIDO")

print("CONTINUAR")
