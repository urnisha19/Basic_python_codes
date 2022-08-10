"""HCF(Highest Common Factor)
Factor: When I can divide a number a by b completely then b is said to be a foctor of a.
Higest common factor: the factor that is common between two numbers and which is highest.
"""


def HCF(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a

    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            ans = i
            print(ans)  # last number ta HCF
    return ans


HCF(8, 4)
