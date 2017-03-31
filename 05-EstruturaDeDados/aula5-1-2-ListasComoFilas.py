# 5.1.2 Listas como Filas - Estrutura de dados - Tutorial de Python3 em Português
# https://www.youtube.com/watch?v=yB0etQdRGdc

#importando pacotes
from collections import deque

fila = deque([])
fila.append('Abel')
print(fila)

fila.append('Malcher')
fila.append('Maria')
fila.append('Nayana')
fila.append('Luciana')
print(fila)

# apagar do começo da fila
fila.popleft()
print(fila)

# adicionar no inio da fila
fila.appendleft('José Furão')
print(fila)














