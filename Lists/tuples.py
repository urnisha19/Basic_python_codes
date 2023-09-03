# Tuple example
tup = (1, 2, 3, 4, "hello", 9.9)
print(tup)
print(type(tup))
print(tup[4])
print(tup[:3])

new_list = list(tup)  # tuple ke list e covert
print(new_list)
print(type(new_list))

t = tuple(new_list)  # list ke tuple e convert kora
print(type(t))
