"""write a Area() function, that takes an user input, then correspondingly selects which area to print.
inside the choice, user is again asked to take the req input
E, g Input:
Enter any shape:
circle
Please enter the radius:
output:
The required area is:
The function should be able to print 4 basic shapes: Circle, Rectangle, Square,Triangle and Trapezium
"""


def area_func():
    print(
        "Enter the shape to find the area(e,g circle,triangle, rectangle, square,trapezium): "
    )
    shape = input()

    if shape == "circle":
        print("Please enter the radius: ")
        r = float(input())
        area = 3.1416 * r * r
        print("The area is: " + str(area))
    elif shape == "triangle":
        print("Please Enter the base : ")
        base = float(input())
        print("Please Enter the height: ")
        height = float(input())
        area = 0.5 * base * height
        print("The area is: " + str(area))
    elif shape == "rectangle":
        print("Please Enter the length: ")
        length = float(input())
        print("Please Enter the width: ")
        width = float(input())
        area = length * width
        print("The area is: " + str(area))
    elif shape == "square":
        print("Please Enter the length: ")
        length = float(input())
        area = length**2
        print("The area is: " + str(area))
    elif shape == "trapezium":
        print("Please Enter the side 1 : ")
        side1 = float(input())
        print("Please Enter the side 2 : ")
        side2 = float(input())
        print("Please Enter the height : ")
        height = float(input())
        area = 0.5 * (side1 + side2) * height
        print("The area is: " + str(area))
    else:
        print("invalid input shape")


area_func()
