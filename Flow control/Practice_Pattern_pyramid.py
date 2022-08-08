"""
    *
  ***
 *****
*******
"""
print("please enter the number of row")
number_of_row = int(input())
count = 0

for current_row in range(0, number_of_row):
    for space in range(number_of_row - current_row - 1):
        print(end=" ")  # end=" "==> without new line simply a space print
    count = count + 1  # end of 2nd loop

    for star in range(0, current_row + count):
        print("*", end="")  # end="" ==> just print star then avoid a new line with end=""
    print(" ")  # a new line
