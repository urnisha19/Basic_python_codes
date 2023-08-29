# Write a recursive function to do integer exponentiation. if x and y are integers, then you are to find out the value of x^y
"""
input: 2 3
output: 8
"""

def exponent(x,y):
    if y == 0:
        return 1
    else:
        return x*exponent(x, y-1)

print(exponent(2, 3))

# Another version
def exponent2(x, y):
    if y == 0:
        return 1
    elif y %2 == 0:
        return exponent2(x, y//2)*exponent2(x, y//2)
    else:
        return x*exponent2(x, y//2)*exponent2(x, y//2)

print(exponent2(2, 4))