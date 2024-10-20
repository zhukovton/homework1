# словарь - набор элементов ключ: занчение
# a = {
#     1: "11",
#     2: "22",
#     3: "33",
#     "surname": "Zhukov",
#     "name": "Tony"
# }
# Сущ. ключ. По ключу выводим значение
# print(a["name"])
#
# # Создаем новую пару
# a["name2"] = "Dimon"
# print(a)


# # Используем, когда точно не знаем есть ли ключ в словаре
# print(a.get(1))
# print(a.get(1, "Net znachenia"))


# print(a.keys())
# print(a.values())
# print(a.items())

# for key in a.keys():
#     print(key)
#
# for value in a.values():
#     print(value)
#
# for key, value in a.keys():
#     print(key, value)


# 3n + 1  Заполнить ключ значение

a = {

}

# ключи от 0 до 10
# for key in range(10):
#     a[key] = 3*key + 1
#
# print(a)


str1 = input("Ввести: ")

# Для каждого символа посчитать кол-во вхождений Ключ будет символом стки, Знчение - кол-во вхожд. этого символа
for i in str1:

     if i in a:
         a[i] += 1
     else:
         a[i] = 1

print(a)