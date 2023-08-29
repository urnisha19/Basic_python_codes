"""
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

for i in range(0,5):
    print(fib(i), end=" ")


l = []
def convert_number(num):
    if(num == 0):
        return 1
    digit = num % 2
    l.append(digit)
    convert_number(num-2)

convert_number(6)
l.reverse()
for i in l:
    print(i, end="")
"""

def summation(num_list):
    if len(num_list) == 0:
        return 0
    if num_list[-1] % 2 == 0:
        return num_list[-1]+ summation(num_list[:-1])
    else:
        return summation(num_list[:-1])

a = summation([1,2,3,4,6,10,11,121,1009])
print(a)