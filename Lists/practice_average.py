"""
Given a list of number(might be sorted or unsorted), return the centered avg of the numbers. It's the average formed by excluding the largest and the smallest values all together.
input:
1 2 3 4 5
Otput:
3
"""


def centered_average(some_list):
    sum = 0
    count = 0
    temp_list = some_list.sort()
    for i in range(1, len(some_list) - 1):
        sum = sum + some_list[i]
        count = count + 1
    return sum / count


a = [1, 2, 3, 4, 5]
print(centered_average(a))
