# Аргументы позизионные и ключевые
# a = 5
# print(a, 4, 5, 6, sep=" ")  # a, 4, 5, 6, - позиционные sep - ключевые


# def my_func(x, second):
#     print(x, second)
#
#
# my_func(5, 7)
# my_func(5, second=7)

# Функция получает на вход список чисел
# и два индекса. Вернуть сумму чисел между
# между переданными индексами.
# Если индекс выходит за пределы списка,
# сумма считается до конца и/или начала списка.
# Если нижняя граница меньше нуля, суммируем от начала.
# Если верхняя граница больше длины списка, до конца.

def particial_sum(numbers: list[int], first_index: int, second_index: int) -> int:

    """
    Функция, которая выводит сумму элементов между двумя индексами
    """
    if first_index > second_index:
        # поменяли переменные местами
        first_index, second_index = second_index, first_index
    if first_index < 0:
        first_index = 0
    default_right_border = len(numbers) - 1
    if second_index > default_right_border:
        second_index = default_right_border

    result = 0
    for i in range(first_index, second_index + 1):
        result += numbers[i]

    return result


nums = [1, 2, 3, 4]
li = 2
ri = 5

print(particial_sum(nums, li, ri))
