# 4.7.6 String de Documentação e __doc__ - Tutorial de Python 3 em Português
# https://www.youtube.com/watch?v=bNbZ8v-V-tM
from builtins import print


def exemplo():
    """
    Documentação em várias linhas
    
    :return: 
    """
    pass

print(exemplo.__doc__)


#impressão dos docs helps
print(print.__doc__)

print(int.__doc__)


