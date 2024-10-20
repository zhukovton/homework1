# Кортеж. Отличается от списка тем, что мы не можем  изменять его длину
# tuple1 = (1, 2, 3)

# Строки
name = "Tony"
surmane = "Zhukov"
# print(name[0])
# print(name + surmane)
#
# # Срезы
# print(name[0:7:2])
#
# # f - string
# print(f"{name} {surmane}")
# # Вывыод переменной с равно
# print(f"{name=} {surmane=}")

# name = name.replace("o", "F", 2) # без третьего аргумента заменит все совпадения, с арг. Заменить указанное количество
# print(name)
# print(name.title()) # с большой буквы
# print(name.split())


# path = "dsfds/dsfdsf/sdfsdf"
# print(path.split("/"))

# input_nums = input().split()
# print(input_nums)

nums = [1, 2, 3, 4, 5, 6]
print(nums.index(4)) # 4 - это значение, вывод будет его индекс в массиве
if 3 in nums:
    print(nums.index(3))




