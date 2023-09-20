# operadores lógicos
# and (e) or (ou) not (não)
# or - qualquer condição verdadeira avalia toda a expressão como verdadeira
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor
# # São considerados falsy
# 0 0.0 '' False
# None - usado para representar um não valor

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")
senha_permitida = "123456"

if (entrada == "E" or entrada == 'e') and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")

# Avaliação de curto circuito - o python verifica o código até chegar no False, não lê mais nada para frente

#print (0 ar False or 'abc' or True)


#senha = input ('Senha: ') or 'Sem senha'
#print (senha)