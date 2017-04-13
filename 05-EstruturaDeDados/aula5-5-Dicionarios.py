# 5.5 Dicionários - Tutorial de Python 3 em Português
# https://www.youtube.com/watch?v=BEC3yRG57UI&t=3s

# http://www3.ifrn.edu.br/~jurandy/fdp/doc/aprenda-python/capitulo_10.html#capitulo-10-dicionarios

dicionario = {'jose': 32 , 'Chave': 'valor'}
print(dicionario)

dicionario['Nome'] = 'Jose'

print(dicionario)

dicionario['Sobrenome'] = 'Malcher'

print(dicionario)

#somente as chaves
print(sorted(dicionario))

print(dicionario.keys())

print(tuple(dicionario.keys()))

print('jose' in dicionario)


print(dict(nome='jose', idade=32))

print(dict([('quadrado',4),('bolinha',1)]))
