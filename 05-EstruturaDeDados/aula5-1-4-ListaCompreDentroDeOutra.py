# 5.1.4 Lista por Compreensão dentro de outra - Tutorial de Python 3 em Português
# https://www.youtube.com/watch?v=LNWuLNXVM2E




matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],]
print(matriz)

matriz2 = [[lin[i] for lin in matriz] for i in range(4)]

print(matriz2)

matriz3 = list(zip(*matriz))
print(matriz3)