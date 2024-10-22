# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
nums = [1, 2, 3, 4, 6, 1, 7]
# => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д

def posledovat(nums: list[int]) -> list[int]:
    result = [nums[0]]
    for i in range(1, len(nums)):
        # print(i)
        if nums[i] > result[-1]:
            print(nums[i])
            result.append(nums[i])
    return result


print(posledovat(nums))

