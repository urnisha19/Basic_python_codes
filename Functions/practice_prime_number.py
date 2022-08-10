# Write a function to check if a number is prime or not(use divisibility)
# The number which are not divisible by any other number except themselves are called prime numbers
import math


def check_prime(n):
    count = 0
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            print("Not prime")
            break
        count = count + 1
    if count + 2 == math.floor(math.sqrt(n)) + 1:
        print("Prime")


print("Enter the number: ")
n = int(input())
check_prime(n)
