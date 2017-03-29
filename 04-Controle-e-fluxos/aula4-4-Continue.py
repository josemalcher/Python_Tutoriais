# 4.4 continue (Parte 3) - Tutorial de Python 3 em Português
# https://www.youtube.com/watch?v=UDDDNCR7-KY

for n in range(10):
    if n == 4:
        continue
    print(n)
print("Fim FOR")

print("\n-------------------------\n")


a = 0
while a <= 10:
    print(a)
    a += 1
    if a == 5:  # não faz diferença...
        continue


print("Fim WHILE")

