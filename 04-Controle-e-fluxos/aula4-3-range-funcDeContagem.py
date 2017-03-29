# 4.3. range() - Função de Contagem - Tutorial de Python 3 em Portugues
# https://www.youtube.com/watch?v=ycSu1mYonhI

for numero in range(5):
    print(numero)

for numero in range(1, 11):
    print(numero, end=', ')

print("\n###########################\n")


for numero in range(2, 21,2): #pula de 2 em 2
    print(numero, end=', ')

print("\n###########################\n")

contagem = list(range(1,21))
print(contagem, end=', ')

print("\n###########################\n")

contagem = list(range(10, -11, -1))
print(contagem)

print("\n###########################\n")

nomes = ['abel', 'frederico', 'jose', 'malcher','joana','maria']
for nome in range(len(nomes)):
    print(nome, nomes[nome])
