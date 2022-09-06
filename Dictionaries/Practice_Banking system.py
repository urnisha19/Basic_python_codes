"""
A simple banking system database:
Create dictionary of users with their balance.
Create options to modify the database:
1. view the balance
2. View all info
3. Update balance
If the user doesn't exist, keep an option to add the user to the database_system. Keep option to exit instead of this.
"""
bank_users = {'Alice': 1233, 'Samee': 2500, 'Robert': 30000}

print('Welcome to the bank')
while True:
    print('What do u like to do?')
    print(' ' + '1. View balance')
    print(' ' + '2. View all bank info')
    print(' ' + '3. Update balance')
    print(' ' + '4. Exit')

    decision = input()
    if decision == '1':
        print('Enter your name please: ')
        name = input()
        if name in bank_users.keys():
            print(name + ' Your bank balance is ' + str(bank_users[name]))
        else:
            print('The user can not be found. Would u like to add the user to the account?')
            decision = input()
            if decision == "Yes":
                name = input('Enter your name: ')
                balance = input('Enter your balance: ')
                bank_users.update({name: balance})
            else:
                print('Would u like to exit?')
                decision = input()
                if decision == 'Yes':
                    break
    elif decision == '2':
        for name, balance in bank_users.items():
            print('UserName: ' + str(name) + ' Bank Balance: ' + str(balance))
    elif decision == '3':
        print('Enter your name: ')
        name = input()
        if name in bank_users.keys():
            print('Do u want to add or subtract from savings?')
            decision = input()
            if decision == 'Add':
                temp_balance = bank_users[name]
                extra = input('Enter the amount u want to add: ')
                bank_users[name] = temp_balance + int(extra)
                print('Balance updated. It is: ')
                print(bank_users[name])
            elif decision == 'Subtract':
                temp_balance = bank_users[name]
                extra = input('Enter the amount u want to subtract: ')
                bank_users[name] = temp_balance - int(extra)
                print('Balance updated. It is: ')
                print(bank_users[name])
        else:
            print('There is no such account in the database')
    elif decision == '4':
        break
