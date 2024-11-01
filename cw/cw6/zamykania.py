# внутри функции можно замкнуть другую функцию и аргументы

def plus_string_func(_str):
    counter = 0

    def func(origin):
        return _str + origin, counter

    return func


def age_filter(age: int):
    def __filter(x):
        return x["age"] >= age
    return __filter


# plus_str вернут внутр функцию
func_a = plus_string_func("Hello ")
a = func_a("Vlad")
b = func_a("Alex")
c = func_a("Danila")
# print(f"{a=} {b=} {c=}")

people = [
    {
        "name": "Vlad",
        "age": 22,
        "adress": "NN"
    },
    {
        "name": "Alex",
        "age": 30,
        "adress": "NN"
    },
    {
        "name": "Danila",
        "age": 40,
        "adress": "NN"
    }
]

filter25 = age_filter(25)
print((list(filter(filter25, people))))
