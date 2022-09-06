"""
Write a program to print the unique values of a dictionary.(You must use two dictionary to do this
1 2 3 3 4 5 6 6 6 7
1 2 3 4 7
"""
a = {1: 1, 2: 2, 3: 1, 4: 34}
b = {}  # a dictionary er non-repeating value gulo print hobe
count = {}  # a dictionary er kun value koto bar ase tar frequency count. a dictionary er key gulo count er value hobe.

for i in a.values():
    count.setdefault(i, 0)
    count[i] = count[i] + 1
print('Count: ', count)
i = 0
for k, v in count.items():
    if v == 1:
        b.update({i: k})
        i = i + 1
for i in b.values():
    print(i, end=" ")
