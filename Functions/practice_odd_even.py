# Write a function to check if a number is odd or even(use divisibility)


def check_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("odd")


print("Enter the number: ")
n = int(input())
check_even_odd(n)
