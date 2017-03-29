# Abel Separovich
# 3.2.1 Múltiplas Atribuições
# 3.2.2 Atribuição e Fibonacci (Correção e adendo)
# https://www.youtube.com/watch?v=T37_w-FZg0E

a = 1
b = 2
c = 3

print(a,b,c)

a,b,c = 4,5,6
print(a,b,c)

#no modo interativo (4,5,6) 3 tuplas

a, b = 0, 1
a, b = b, a + b
print(a)
print(b)

a, b = b, a + b
print(a,b)

a, b = b, a + b
print(a,b)

a, b = b, a + b
print(a,b)