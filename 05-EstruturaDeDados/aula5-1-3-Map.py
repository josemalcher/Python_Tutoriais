# 5.1.3 map() (Parte 1) - Tutorial de Python 3 em Português
# https://www.youtube.com/watch?v=phwfKemvyjQ


# map(funcao, *sequencia) --> objeto map

def qua(x) : return x**2

mapa = map(qua,[1,2,3,4,5]) # aqui são COLCHETES

listmap = list(map(qua,[1,2,3,4,5]))

ran = tuple(map(qua,range(10)))

lamb = list(map(lambda x: x**3, range(10)))

print('map(...) = ', mapa)

print()

print('list(map...)) = ', listmap)

print()

print('tuple(map(..., range())) = ', ran)

print()

print('map(funcao lambda,...) = ', lamb)