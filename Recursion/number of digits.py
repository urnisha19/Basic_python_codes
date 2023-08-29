# Write a recursive function to calculate the number of digits in a number using recursion.
"""
input: 1234
output: 4
"""

def digit_counter(n):
    if n == 0:
        return 0
    return 1+digit_counter(n//10) # n//10 means integer division

print(digit_counter(1234))