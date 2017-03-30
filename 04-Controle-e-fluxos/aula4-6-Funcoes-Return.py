# 4.6 return - Funções (Parte 3) - Tutorial de Python 3 em Português
# https://www.youtube.com/watch?v=5MfcMveOMuk

def contatem(ate):
    lista = []
    for num in range(1, ate + 1):
        lista.append(num)
    return lista
print(contatem(10))