"""
An Armstrong number is one whose sum of digits raised to the power three equals the number itself. 371, for example, is an Armstrong number because 3**3 + 7**3 + 1**3 = 371.
Check a number is armstrong or not?
153 = 1^3+5^3+3^3
we would onl consider a three-digit number as an input, and check.
We can obtain each of the digit from a number using the mod operation with a certain number. output will be "yes" or "No"
"""
print("Enter the number")
digit = int(input())
temp = digit
sum = 0

while digit != 0:
    digit_mod = digit % 10
    digit = digit // 10
    sum = sum + digit_mod ** 3

if sum == temp:
    print("Yes armstrong")
else:
    print("Not armstrong")
