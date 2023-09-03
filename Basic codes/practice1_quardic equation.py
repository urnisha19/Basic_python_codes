# Solving Quadratic equation x^2-5x+6. solution = x?

import math

print("enter the coefficients a, b, c:")
a_str = input()
b_str = input()
c_str = input()

# converting input strings into int
a = int(a_str)
b = int(b_str)
c = int(c_str)


# formula
D = math.sqrt(b * b - 4 * a * c)

# ans
x1 = (-b + D) / (2 * a)
x2 = (-b - D) / (2 * a)
print(x1)
print(x2)
