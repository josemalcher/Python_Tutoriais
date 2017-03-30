# 4.6 Variável Local - Funções (Parte 2) - Tutorial de Python 3 em Português
# https://www.youtube.com/watch?v=M4DrgPIzO4Q&t=6s

def exemplo(n):
    a, b = 0, 1

    while a < n:
        print(a, end=', ')
        a, b = b, a + b
    print()


# Repete a função
while True:
    #Pede um numero Limite
    m = int(input('Sequencia de Fib até quanto?  '))
    exemplo(m)