nested_list = [['p', 'q', 'r'], 1, 2, 3, [100, 121, [11, 12, 13]]]
print(nested_list[4][2][2])

aList = [5, 10, 15, 25]
print(aList[::-2])

import copy as cp
s = [10, 20]
s.append(60)
n = cp.copy(s)
n.append(60)
x = cp.copy(n)
x.append(60)
print(s, n, x, sep='#')

sample = [1, 2, 3, 4, 5, 6]
print(sample[:])
print(sample[-1])
