def reverse_list(A):
    new_list = []

    for i in range(0, len(A)):
        new_list.append(0) 

    for i in range(len(A)-1, -1, -1): # len(A)-1 last element er index theke -1 index porjonto jabe. arekta -1 dara -1 ghor kore piche jabe
        new_list[len(A)-1-i] = A[i]

    return new_list

lists = [1, 2, 3, 4]

print(reverse_list(lists))

# reverse string using recursion
def reverse_list_recursive(some_list):
    if len(some_list) == 0:
        return []

    return [some_list[-1]]+reverse_list_recursive(some_list[:-1])

print(reverse_list_recursive(lists))