# 5.4 set (Parte 2)- Tutorial de Python 3 em Português
# https://www.youtube.com/watch?v=apKmo9j1mi4

g1 = set('abel')
g2 = set('papel')
print(g1)

print(g1 - g2)
print(g1 | g2)
print(g1 & g2)
print(g1 ^ g2)

# Set por compreensão

print( {x for x in range(123,1234) if (x % 3 == 0)} )






