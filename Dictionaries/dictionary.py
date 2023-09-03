my_stuff = {"book": "cookbook", "phone": "iphone", "home": "Bangladesh"}
print(my_stuff["book"])

x = {0: 100, 1: 200, 3: 400}
print(x[1])

# in list
a = [1, 2, 3]
b = [2, 3, 1]
print(a == b)

# in dictionary
c = {1: 100, 2: 200, 3: 300}
d = {2: 200, 3: 300, 1: 100}
print(c == d)

# concatenating two dictionaries
x = {1: 100, 2: 200}
y = {4: 500, 6: 600}
new_dic = x.copy()  # x dictionary new dictionary te copy hoye jabe
new_dic.update(y)  # new dictionary update hoye y dictionary add hobe
print(new_dic)
