# 4.7.2 Keywords - Tutorial de Python 3 em português
# https://www.youtube.com/watch?v=4H9pNCv9vJE

def exemplo(a, b = '1'):
    pass

# exemplo()
# TypeError: exemplo() missing 1 required positional argument: 'a'

# exemplo(a='1', '3')
# SyntaxError: positional argument follows keyword argument

# exemplo('a', b = 'b')
# exemplo('1', a='3')
# TypeError: exemplo() got multiple values for argument 'a'

