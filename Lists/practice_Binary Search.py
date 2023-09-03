"""
Perform a Binary search on a list
Here is the algorithm
First sort the list of numbers
If the number asked to find is greater than the last element on the sorted list, then the number doesn't exist.
Else, do the following:
First, check if the number is equal to the middle element of the list or if it's equal, then the number is found.
If it's smaller, then the number must be in the left sublist of the middle number.
If it's larger, then the number must be in the right sublist, search for it there.
Do this until the left sublist is less than the right one
"""


# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1


def binary_search(list, x):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if list[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif list[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


# Test array
list = [2, 3, 4, 10, 40]
print("Enter the value searched for: ")
value_searched = input()
x = int(value_searched)

# Function call
result = binary_search(list, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
