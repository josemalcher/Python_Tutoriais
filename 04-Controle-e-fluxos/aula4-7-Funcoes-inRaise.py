# 4.7.1 in e raise - Funções (parte 3 ) - Tutorial python 3 em Portugues
# https://www.youtube.com/watch?v=ffEwcOg3ulI

def perg_ok(perg, tentativas= 3, lembrete= 'Por favor, responde sim ou não'):
    ok = input(perg)
    if ok in ('s', 'S', 'Sim', 'sim', 'SIM'):
        return True
    if ok in ('n', 'N', 'nao', 'Nao', 'Não'):
        return False
    tentativas = tentativas - 1
    if tentativas < 1:
        raise ValueError('Resposta do usuario inválida')
    print(lembrete)

if perg_ok('Quer continuar?') != True:
    print('Codigo não continuado')
else:
    print('Codigo continuado')