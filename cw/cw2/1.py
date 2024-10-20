#
# list = [1, 2, 3, 5]
#
# print(list[0])
# print(list[-1])
# print(list[3])
#
# # Добавить элемент в конец списка
# list.append(10)
# print(list)
#
# # Добавить в список 1 - позиция, 20 - элемент
# list.insert(1, 20)
# print(list)

# Сложение списка


# print(list2 + list1)

# list1.remove(3)
# print(list1)

# Проверка наличия элемента в списке
# print(3 in list1)


# Удаление элемента
# while 3 in list1:
#     list1.remove(3)

# Удаление элемента по индексу
# list1.pop(3)
# print(list1)


# Узнать Длину списка
# print(len(list1))

# for i in range(len(list1)):
#     print(list1[i])

# for i in list1:
#     print(i)

list1 = ["1", 2, 3, 4, 3, True]
list2 = [4, 5, 6]

n = 3

for i in list1:
    if i == n:
        print(True)
        break
else:
    print(False)



