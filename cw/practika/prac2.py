# Дана последовательность объектов.
# В этой последовательности есть подпоследовательности
# подряд идущих повторяющихся элементов.
# Подпоследовательности необходимо сжать в пары:
# количество повторений в данном месте и объект повторения.
# Реализовать с использованием функции.
# Примеры на строках :
# input: ааа, out: [(3, 'a')] -
# input: aaabbcaac, out: [(3, 'a'), (2, 'b'), (1, 'c'), (2, 'a'), (1, 'c')

input_value = "aaabbcaac"
list_out = []

start_i = input_value[0]
count_i = 0

for i in input_value:
        if i == start_i:
            count_i += 1
        else:
            list_out.append((count_i, start_i))
            start_i = i
            count_i = 1
else:
    list_out.append((count_i, start_i))

print(list_out)





