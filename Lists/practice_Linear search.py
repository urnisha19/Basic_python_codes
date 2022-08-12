"""
Linear search within a list. Given a list, search for a number within the list. If it is found then print "yes", else print "no"
"""


def linear_search(some_list, value):
    for i in range(len(some_list)):
        if some_list[i] == value:
            return "Yes, found"

    if i == len(some_list) - 1:
        return "no, not found"


a = [1, 2, 3, 4, 5, 6]
print(linear_search(a, 33))
print(linear_search(a, 2))
