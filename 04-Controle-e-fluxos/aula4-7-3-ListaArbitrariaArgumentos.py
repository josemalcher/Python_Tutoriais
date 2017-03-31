# 4.7.3 Lista arbitraria de argumentos - Tutorial de Python em Português
# https://www.youtube.com/watch?v=rSaVBCMHUOU


def ajunte(*args, sep="/"):
    return sep.join(args)

a = ajunte('c:','windows','system32','logfiles')

print(a)