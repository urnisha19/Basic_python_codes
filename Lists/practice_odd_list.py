"""
Given a list of numbers, print only odd ones, forming a new list
input:
1 2 3 4 5 6
output:
1 3 5
"""


def print_odd(some_list):
    new_list = []

    for i in range(len(some_list)):
        if some_list[i] % 2 != 0:
            new_list.append(some_list[i])
    return new_list


a = [1, 2, 3, 4, 5, 6]
print(print_odd(a))
