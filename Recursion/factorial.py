# A function to calculate the factorial number
# factorial is basically a product
# 4! = 4x3x2x1
# 4! = 4x3!
# 2! = 2x1

'''
# factorial without recursion
def factorial(n):
    temp = 1
    for i in range(2, n+1):
        temp = temp*i
    
    return temp
print(factorial(int(num)))
'''

# factorial with recursion
def factorial2(n):
    if n == 1: #base case
        return 1
    return n*factorial2(n-1)

num = input()
print(factorial2(int(num)))