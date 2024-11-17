dic = {
    "a": 1
}

print(dic.get("a"))
print(dic.get("b"))


# функция принимает словарь, ключ и базовое значение, если ключ есть вернуть значение, если нет, то базовое
def my_get(dic, key, value=None):
    try:
        return dic[key]
    except KeyError:
        return value


print(my_get(dic, "b", 4))
