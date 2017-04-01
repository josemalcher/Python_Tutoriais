# 5.1.3 Compreensão de listas (Parte 3) - Tutorial de Python 3 em Português
# https://www.youtube.com/watch?v=RuGFo3K4MvQ

# Função para cada item
fun = [abs(x) for x in [-2,-1,0,1,2]]

#lista ou tupla
tup = [(y,y**2) for y in range (1,11)]

# Loop com Loop
lista1 = []
for a in range(4):
    for b in range(4):
        if a != b:
            lista1.append([a,b])

lista2 = [[a,b] for a in range(4) for b in range(4) if a != b]


print(fun)
print(tup)
print(lista1)
print(lista2)


