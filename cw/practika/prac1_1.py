# Напишите программу, которая принимает на
# вход число N и выдает набор произведений чисел от 1 до N.
#  Пример:
# пусть N = 4, тогда [1, 2, 6, 24] (1, 12, 123, 1234)
list1 = []
N = 4
res = 1
for i in range(1, N+1):
    res *= i
    list1.append(res)
print(list1)