# this program simulates a password-protected app access

password_bank = {"Sam": 1234, "Smith": 909090, "Ruth": 120987}
matched = False
x = 0  # loop control variable

print("Enter your name: ")

while x < 5:
    name = input()
    if name in password_bank:
        for i in range(0, 3):
            print("Enter your password: ")
            password = input()
            if int(password) in password_bank.values():
                matched = True
                print("Access Granted")
                break
            else:
                print(
                    "Wrong password. Enter again: "
                    + " you have "
                    + str(2 - i)
                    + " tries left"
                )
    else:
        print("There is no such name in password_bank. Try again")
    x = x + 1
    if matched:
        break
