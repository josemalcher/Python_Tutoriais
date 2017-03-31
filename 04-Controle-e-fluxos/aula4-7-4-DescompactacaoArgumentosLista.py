# 4.7.4 Descompactação de Argumentos em Lista - Turotial de Python 3 em português
# https://www.youtube.com/watch?v=52evIF7kEE4

lista = [1,21]

print(lista)

# list(range(lista))
# TypeError: 'list' object cannot be interpreted as an integer

# list(range([1,21]))
# TypeError: 'list' object cannot be interpreted as an integer

# list(range(*lista))
print(list(range(*lista))) # * -> descompata lista/tupla

# list(range(**dicionario)) # ** -> descompata dicionário
