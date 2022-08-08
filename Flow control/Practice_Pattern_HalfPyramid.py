"""
   *
  **
 ***
****
"""
print("please enter the number of row")
number_of_row = int(input())

for current_row in range(0, number_of_row):
    for space in range(number_of_row - current_row - 1):
        print(end=" ")  # end=" "==> without new line simply a space print

    for star in range(0, current_row + 1):
        print("*", end="")  # end="" ==> just print star then avoid a new line with end=""
    print(" ")  # a new line
