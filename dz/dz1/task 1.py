# 1) Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

n = int(input("Введите номер четверти (1-4): "))
if n == 1:
    print("x >= 0 and y >= 0")
elif n == 2:
    print("x <= 0 and y <= 0")
elif n == 3:
    print("x >= 0 and y <= 0")
elif n == 4:
    print("x <= 0 and y >= 0")
else:
    print("Четверти с таким номером не существует, только 1,2,3,4")
