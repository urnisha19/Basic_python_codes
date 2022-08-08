"""
Condition:
if year is divisible by 400 then is_leap_year
if year is divisible by 100 then not_leap_year
if year is divisible by 4 then is_leap_year
"""
year = int(input("Enter the year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not Leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not Leap year")
