# 5.6 Técnicas de Loop - Tutorial de Python 3 em Português
# https://www.youtube.com/watch?v=LXv6d07Bqlw

dicionario = {'nome':'jose malcher','curso': 'Eng. Softwate', 'nacimento':'1984'}

for k, v in dicionario.items():
    print(k, ', ',v)

for n, v in enumerate(['um','doi','tres']):
    print(n,v)

assunto = ['virtualização','VM','Java']
definicao = ['feramenta tal tal tal tal tal tal', 'vm é tal tal tal','java é tal tla tal tla']

for a, d in zip(assunto, definicao):
    print('o que é {0} -> {1} . '.format(a,d))


for n in reversed(range(1,6)):
    print(n)

frutas = ['abacaxi','melão', 'limão', 'Pera', 'Banana', 'abacaxi','pera']
for f in sorted(set(frutas)):
    print(f)


import math

dado_bruto = [56.2, float('NaN'),51.7, 55.3, 52.5, float('NaN'),47.3]
dado_filtrado = []

for valor in dado_bruto:
    if not math.isnan((valor)):
        dado_filtrado.append(valor)
print(dado_filtrado)