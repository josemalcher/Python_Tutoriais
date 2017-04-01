# 5.1.3 Compreensão de listas (Parte 2) - Tutorial de Python 3 em Português
# https://www.youtube.com/watch?v=fEC6Hocz_lg

squares = []
for x in range(10) :
    squares.append(x**2)

# é igual a

squares = list(map(lambda x: x**2, range(10)))

# Melhorando

squares = [x**2 for x in range(10)]

#Explicando

# list(map(função, sequencia))
# list(map(lambda  x: x * 7, range(11)))

# devolver for x in sequencia
# [x*7 for x in range(11)]

##### Exemplo

quadrados = []
for x in range(10):
    quadrados.append(x**2)

quadrado = list(map(lambda y:y**2, range(10))) # Aula Passada

qua = [z**2 for z in range(10)] # forma mais simples

print(quadrados)
print(quadrado)
print(qua)

tabuada7 = [x * 7 for x in range(1,11)]
print(tabuada7)