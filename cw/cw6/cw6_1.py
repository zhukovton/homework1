# Функции высшего порядка  - Функция, котороая принимает в себя функцию,
# как параметр


# def pass_func(x):
#     if int(x) >= 5:
#         return True
#     return False
# Вместо такого варианта, можно написать:

def pass_func(x):
    return int(x) >= 5


def is_all_valid(func: callable, _lst) -> bool:
    for i in _lst:
        if not func(i):
            return False
    return True


_lst = ["1", "2", "3", "234", "33333"]

filtered = list(filter(pass_func, _lst))

# print(filtered)

print(is_all_valid(pass_func, _lst)) # pass_func передаем без скобок,
# т.к. хотим её вызвать как объект, а не вызвать её


