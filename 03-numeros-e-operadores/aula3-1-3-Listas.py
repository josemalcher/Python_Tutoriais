#3.1.3 Listas (Parte 1) Python 3.5 Tutorial
#
#https://www.youtube.com/watch?v=BZYZzAvcoHk


# [1,2,3,4,5]
# ['sabão','arroz']

quadrado = [1,4,8,12,25]
print(quadrado[0],quadrado[1])
print(quadrado[-1])
print(quadrado[1:2]) # retorna outra lista

# mudar valor
quadrado[-1] = 26
print(quadrado[-1])

# método append
quadrado.append(36)
print(quadrado)

# operação
quadrado.append(7**2)
print(quadrado)

print(len(quadrado))

# Concatena
letra = ['a','b','c''d']
alfa = ['a','u']
totalLetras = alfa + letra
x = [letra,alfa]
print(letra + alfa)
print(totalLetras)
print(x)

totalLetras[0] = 1
print(totalLetras)

letra01 = [[1,2,3],[4,3,2,1]]
print(letra01)

