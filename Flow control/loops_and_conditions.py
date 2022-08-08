# use of infinite loop
while True:
    print("please enter your name")
    name = input()
    if name == 'your name':  # the loop will execute infinity times, and will stop only when we enter "your name" in the input
        break
print("thank you")

# use of continue statement
while True:
    print("Who r u?")
    name_2 = input()
    if name_2 != 'Batman':
        continue
    print("Hello " + name_2 + " what is the passcode?")
    passcode = input()
    if passcode == 'icecreamtrack':
        break
print("successfully entered")

