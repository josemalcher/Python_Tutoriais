# 5.1 Métodos de listas (Parte 1) - Tutorial de Python 3 em Português
# https://www.youtube.com/watch?v=dbu9tft6nok

a = [1,2,3]
print(a)
a.append(4)
print(a)

# remove do final ou pop(local)
a.pop()
print(a)

#inserir no local insert(local,valor)
a.insert(0,10)
print(a)


a.append(2)
print(a)
#remover valor, ele pega o primeiro que vier na lista
a.remove(2)
print(a)

#limpar toda  alista
a.clear()
print(a)

# ou

del a[:]
print(a)



