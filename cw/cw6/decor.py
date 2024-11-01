# дополнение функционала функции,
# без вмешивания работы самой функции

def deco(func: callable):
    cache = {}
    def wrapper(*args, **kwargs):
        cache_key = str(args)+str(kwargs)
        if cache_key in cache:
            print(" Сработал кэш")
            return cache[cache_key]
        result = func(*args, **kwargs)
        cache[cache_key] = result
        print((f"{cache=}"))
        return result
    return wrapper

@deco  # синтаксический сахар
def sum_of_two(x, y):
    return x + y

@deco
def filter25(x):
    return x > 25

# # funx = deco(sum_of_two)
# print(sum_of_two(3, 4))
# print(sum_of_two(3, 4))
# print(sum_of_two(3, 3))
# print(sum_of_two(5, 3))
# print(sum_of_two(10, 10))
# print(sum_of_two(5, 3))
print(filter25(30))
print(filter25(35))
print(filter25(30))

