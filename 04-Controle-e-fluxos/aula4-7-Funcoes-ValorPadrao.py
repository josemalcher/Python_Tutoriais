# 4.7.1 Valor Padrão - Funções (parte 2) - Tutorial de Python em Português
# https://www.youtube.com/watch?v=VPy2LgiX500

def exemplo(n1 = 20, n2 = 30, n3 = 40):
    print(n1)
    print(n2)
    print(n3)

exemplo()
exemplo('teste')
exemplo(n3='outro valor')

def exemplo2(n1, n2 = 30, n3 = 40):
    print(n1)
    print(n2)
    print(n3)
exemplo2("é necessário um argumento")