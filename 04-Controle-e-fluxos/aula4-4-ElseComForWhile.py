# 4.4 Else com For e While (Parte 1) - Tutorial de Python 3 Português
# https://www.youtube.com/watch?v=tdgn_uzOgHs

# Uma contagem de pique Esconde
print("Vou contar!")

#Loop de contagem.
for vari in range(1, 11):
    print(vari, end=', ')
else:
    print("PRONTO, TO INDO!!")

#Fim do codódigo
print("Fim do programa")

print("\n ############################### \n")

b = int(input("Escreva um número entre 0 e 10: "))
while b <= 10:
    print(b)
    b += 1
else:
    print("FIM")