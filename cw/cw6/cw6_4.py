# функ, которая принимает на вход 2 функции и элемент x
# и выполнит сначала f потом g и возвращает х

def funf(f: callable, g: callable, x):
    f_result = f(x)
    return g(f_result)


def sq(x):
    return x ** 2


def m5(x):
    return x - 5


x = 5
print(funf(sq, m5, x))
