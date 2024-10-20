# Множество. Хранит уникальные значения. Тип и порядок не важен
set = {4, 3, 2, 1}
set2 = {88, 1, 2, 3, 4, 7}
# print(set)
set.add(7)
# print(set)
# складывание множеств
print(set.union(set2))
# проверка тру/фолс
print(1 in set)

print(set.difference(set2)) # Вычетание
print(set.union(set2)) # Объединение
print(set.intersection(set2)) # Выведен совпадающие значения