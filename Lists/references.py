import copy as cp

a = [1, 2, 3]
b = a  # a list r reference b te copy
b[1] = 3.1416  # b ke modify korle a o modify hobe jabe cz same reference
print(a)


def f(some_list):
    some_list.append('ok')


x = [1, 2, 3]
s = cp.copy(x)  # a copy of the list is made
f(s)

print(x)
print(s)
