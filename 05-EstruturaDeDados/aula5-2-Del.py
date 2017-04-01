# 5.2 del - Tutorial de Python 3 em Português
# https://www.youtube.com/watch?v=RO5S2-Kd0vQ

l = [-1, 0,1,2,3,4]
print(l)
del l[0]

print(l)

del l[1:3]
print(l)

#apagar
del l
print(l) # NameError: name 'l' is not defined