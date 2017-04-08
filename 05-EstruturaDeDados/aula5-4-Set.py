# 5.4 set (Parte 1) - Tutorial de Python 3 em Português
# https://www.youtube.com/watch?v=pGPnPOqC7cc

a = {'Abel', 'laise', 'Abel', 'Alice', 'Jose malcher'}
print(a)
#{'Jose malcher', 'laise', 'Alice', 'Abel'}

print(type(a))

b = {}
print(type(b))
print(b)

c = set()

print(type(c))

a.remove('Alice')
print(a)

a.add('MARIA')
print(a)

print('Abel' in a)
print('Junior' in a)

print('Junior' not in a)