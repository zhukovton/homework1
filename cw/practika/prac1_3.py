# Дан список чисел и целевое число. Вернуть индексы двух чисел из списка которые в сумме дают целевое.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] + nums[j] == target and i != j:
            print(i, j)
            exit()
