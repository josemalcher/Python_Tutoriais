# 4.7.7 Anotação de Funções __annotations__ - Turotial de Python 3 em português
# https://www.youtube.com/watch?v=8QzKLeWHP8s


# def exemplo(arg: tipo) -> tipo :
def exemplo(arg1: int , arg2:int) -> float :
    return float(arg1 * arg2)

print(exemplo(2,3))

print(exemplo(4.5,3))

print(exemplo(10,20))

print(exemplo.__annotations__)





